
import matplotlib as mpl
from matplotlib import rc
import json
from scipy.optimize import basinhopping,minimize
import scipy
import numpy as np
import sys
import scipy.interpolate
from matplotlib import pyplot as plt
plt.ion()

params_fname = sys.argv[-1]
params = json.load(open(params_fname))

n_rows = params['electrode_params']['y_N']
n_cols = params['electrode_params']['x_N']

fname = "data/bundle_pulse_" + params['postfix'] + ".npz"
potentials = np.load(fname)

nodes = potentials['nodes']
node_locs = []
# ngroup =  pot['nodes'][0]
for n, ngroup in enumerate(nodes):
    for m, segment_group in enumerate(ngroup):
        for segment in segment_group:
            segment = np.array(segment)
            node_locs.append(segment)
node_locs = np.vstack(node_locs)
node_hist, node_hist_bins = np.histogram(node_locs[:,0],1000)
node_hist = node_hist.astype(float)
node_hist /= node_hist.max()

locs = potentials['loc']
locs_all = locs.copy()
pots_all = potentials['pot'].copy()
ind_all = locs_all[:,1]>0
locs_all=locs_all[ind_all]
pots_all = pots_all[ind_all]

ind = np.logical_or(locs[:,1]==500., locs[:,1]==2420.)
ind = np.logical_and(ind, locs[:,0] < 22000.)
pots = potentials['pot'][ind]
locs = locs[ind]
pots = pots[:,3000:5000]
# pots_all = pots_all/pots.std()
# pots = pots/pots.std()
t = np.arange(pots.shape[1])*2.5e-4
#z = np.unique(locs[:,0])
z = np.arange(0,20000.,100.)
#z = z[z>=10000.]
z = np.repeat(z[:,np.newaxis],3,1)
z[:,1:] = 0

t = np.repeat(t[:,np.newaxis],z.shape[0],1)
z_all = np.repeat(z[np.newaxis,:],locs_all.shape[0],0)
z = np.repeat(z[np.newaxis,:],locs.shape[0],0)

dists = np.sqrt(np.sum((z-locs[:,np.newaxis,:])**2,axis=2))
w = 1. / dists.T
wmax = w.max()
w /= wmax

dists = np.sqrt(np.sum((z_all-locs_all[:,np.newaxis,:])**2,axis=2))
w_all = 1. / dists.T
w_all /= wmax

pots = pots.T

def symdiff(x):
    ret = np.zeros_like(x)
    diff = np.diff(x,axis=1)
    ret[:,1:] = diff
    ret[:,:-1] += diff
    ret[:,1:-1] *= 0.5
    return ret

def calc_phi(x, w_local=w, z_local=z):
    r = 0.#x[0]
    scale = np.abs(x[0])
    ivel =  -0.0006/100.+1e-10*x[1]/100.
    vdot = x[2:t.shape[0]+2]
    n = np.abs(x[t.shape[0]+2:t.shape[0]+t.shape[1]+2])
    #n /= n.max()
    #n[n<0] = 0.


    #vdot_prop = np.zeros_like(t)
    #phi = np.zeros_like(pots)
    
    vdot_prop = np.zeros((vdot.shape[0],t.shape[1]))
    vdot_prop[:,0] = vdot[:]
    #vdot_prop[:,:] = vdot[:,np.newaxis]
    vdot_inter = scipy.interpolate.interp1d(t[:,0],vdot,fill_value=0.,bounds_error=False)
    for xn in range(1, z_local.shape[1]):
        shift = ((z_local[0, xn, 0] - z_local[0, 0, 0]) * ivel)
        vdot_prop[:,xn] = vdot_inter(t[:,0]+shift)
    phi = np.dot(symdiff(vdot_prop*n), w_local)
    return scale*phi

    #for tn in range(phi.shape[0]):
    #    phi[tn, :] = np.convolve(i[tn,:], w, mode='same')

def func(x):
    phi = calc_phi(x)
    ret = np.sqrt(np.mean(((pots-phi)**2)[200:,20:]))/pots[:,20:].std()
    n = np.abs(x[t.shape[0] + 2:t.shape[0] + t.shape[1] + 2])
    ret += 0.1*np.mean(np.diff(n/n.max())**2)
    ret += 0.1 * np.sqrt(np.mean(x[2:t.shape[0]+2]**2))
    if np.random.random()<0.001:
        print ret,0.1*np.mean(np.diff(n/n.max())**2), 0.1 * np.sqrt(np.mean(x[2:t.shape[0]+2]**2))
        np.savez('data/figS1_fit_tmp.npz',params=x,val=ret)
        # plt.clf()
        # plt.subplot(412)
        # plt.imshow(phi[:,np.logical_and(locs[:,1]<550.,locs[:,0]>=10000.)], aspect='auto')
        # plt.subplot(411)
        # plt.imshow(pots[:, np.logical_and(locs[:, 1] < 550., locs[:, 0] >= 10000.)], aspect='auto')
        # plt.subplot(413)
        # plt.plot(z[0,:,0],n/n.max())
        # plt.plot(node_hist_bins[1:], node_hist)
        # plt.xlim(10000,16500)
        # plt.subplot(414)
        # plt.plot((x[2:t.shape[0]+2]))
        #
        # plt.show()
        # plt.pause(0.01)

    return ret

try:
    fitfile = np.load('data/figS1_fit_tmp.npz')
    x0 = fitfile['params']
except:
    x0 = (np.random.randn(t.shape[0]+t.shape[1]+2))
    #x0[2:t.shape[0]+2] = 0.# -pots.mean(axis=1)
    x0[1] = -0.0006
    n0 = pots[:,np.logical_and(locs[:,1]<550.,locs[:,0]>=10000.)].std(axis=0)
    n0 /= n0.max()
    n0 = 1+0.1*(np.random.randn(t.shape[1]))+5.*np.exp(-((z[0,:,0]-15000)/500)**2)
    #n0 = pots_all[5::30].std(axis=1)[:]
    x0[t.shape[0]+2:t.shape[0]+t.shape[1]+2] = n0
    pred = calc_phi(x0)
    x0[0] = 0.5*pots.std()/pred.std()
print x0.shape

try:
    fitfile = np.load('data/figS1_fit.npz')
    #fitfile = np.load('tmp.npz')
    params = fitfile['params']
except:
    print "Fresh fit."
    ret = minimize(func,x0,options={'maxiter':100,'disp':True})
    params = ret.x
    hinv = ret.hess_inv
    np.savez('data/figS1_fit.npz', params=params, hinv=hinv)

# locs = locs_all
# pots = pots_all
#
# dists = np.sqrt(np.sum((z-locs[:,np.newaxis,:])**2,axis=2))
# w = 1. / dists.T
# w /= w.max()

phi = calc_phi(params)
print "Final fit:",func(params)

phi_full = calc_phi(params,z_local=z_all,w_local=w_all)
pot = pots_all[:,3000:5000].T.reshape(2000,300,29)
phi = phi_full.reshape(2000,300,29)
