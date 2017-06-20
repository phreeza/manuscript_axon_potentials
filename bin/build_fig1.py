import matplotlib
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
#matplotlib.use('Agg')
import numpy as np
from matplotlib import pyplot as plt
from lib.scalebars import add_scalebar

from lib import utils
import glob

lw=2
subfig_fontsize = 12
snip_spacing = 40

def draw_snip(x0,x1,y,slant):
    plt.plot([x0,x1],[y+snip_spacing,y+snip_spacing+slant],color='white',lw=4)
    plt.plot([x0,x1],[y,y+slant],color='black',lw=1)
    plt.plot([x0,x1],[y+2*snip_spacing,y+2*snip_spacing+slant],color='black',lw=1)

pots =  np.load('data/pots.npz')['pots']
pots2 = np.load('data/pots_2.npz')['pots'] #pots3 = np.load('pots_3.npz')['pots'].sum(axis=1)
pots3 = np.load('data/pots_bifterm.npz')['pots']
scale = 5e-3
scale2 = scale*8
scale3 = scale*300
scale4 = scale*6

axes_w = 0.1/3.*4.
axes_h = 0.52
axes_ws = 0.08/3.*4.
axes_hs = 0.46
t = np.arange(pots.shape[1])*0.0025
t3 = np.arange(pots3.shape[1])*0.0025
ax1 = plt.axes([2*axes_w,axes_h,axes_ws,axes_hs]) #plt.subplot(2,8,2*order[n_p]+1,sharey=ax1)
for n in range(80,120,4):
    plt.plot(t,pots[n,:].T/scale-(n-100)*100.,color='black',lw=1)
plt.plot(t,pots[100,:].T/scale,color='black',lw=lw)
plt.xlim(1.4,1.9)
plt.axis('off')

add_scalebar(ax1,sizex=.2,sizey=0.02e6/scale,matchx=False,matchy=False,labelx='0.2 ms',
        labely='20 $\mu$V',loc=1)

plt.axes([4*axes_w,axes_h,axes_ws,axes_hs],sharey=ax1) #plt.subplot(2,8,2*order[n_p]+1,sharey=ax1)
for n in range(180,220,4):
    plt.plot(t,pots[n,:].T/scale-(n-200)*100.,color='black',lw=1)
plt.plot(t,pots[200,:].T/scale,color='black',lw=lw)
plt.xlim(2.0,2.5)
plt.axis('off')

ax2 = plt.axes([6*axes_w,axes_h,axes_ws,axes_hs],sharey=ax1) #plt.subplot(2,8,2*order[n_p]+1,sharey=ax1)
for n in range(80,120,4):
    plt.plot(t,pots2[n,:].T/scale2-(n-100)*100.,color='black',lw=1)
plt.plot(t,pots2[100,:].T/scale2,color='black',lw=lw)
plt.xlim(1.4,1.9)
plt.axis('off')

add_scalebar(ax2,sizex=.2,sizey=0.2e6/scale2,matchx=False,matchy=False,labelx='0.2 ms',
        labely='0.2 mV',loc=8,bbox_to_anchor=(290.5,170.5))

plt.axes([2*axes_w,0.1*axes_h,axes_ws,axes_hs],sharey=ax1) #plt.subplot(2,8,2*order[n_p]+1,sharey=ax1)
for n in range(80,120,4):
    plt.plot(t3,pots3[n,:].T/scale2-(n-100)*100.,color='black',lw=1)
plt.plot(t3,pots3[96,:].T/scale2+400.,color='black',lw=lw)
plt.plot(t3,pots3[104,:].T/scale2-400.,color='black',lw=lw)
plt.xlim(1.4,1.9)
plt.axis('off')

order = [1,0,2,0]
column = [0,0,0,1]
c = ['r','g','b']
d_sep = 20
for n_p in range(4):
    ax = plt.axes([axes_w*(2*order[n_p]+1)+0.017,axes_h-0.9*axes_h*column[n_p],axes_ws,axes_hs],sharey=ax1) #plt.subplot(2,8,2*order[n_p]+1,sharey=ax1)
    plt.arrow(-15,1800,0,-800,width=1,head_width=8,facecolor='black',head_length=100)
    if n_p == 0:
        plt.plot([0,0],[2000,0],color='black',lw=lw)
        plt.plot([0],[0],color='black',lw=lw,marker='o',mec='none',ms=3.5)
        draw_snip(-5,5,1820,10)
    elif n_p == 1:
        plt.plot([0,0],[-2000,2000],color='black',lw=lw)

        draw_snip(-5,5,1820,10)
        draw_snip(-5,5,-1860,10)
    elif n_p == 2:
        y_sep = [0.,100.,100.,1900.]
        x_sep = [20,10,5]
        p = [[[0.,0.] for m in range(2**n)] for n in range(4)]
        p[0][0][1] = 100.
        plt.plot([0,0],[2000,100],color='black',lw=lw)
        for n in range(1,4):
            for m in range(2**n):
                p[n][m][1] = p[n-1][0][1] - y_sep[n-1]
                if m%2 == 0:
                    p[n][m][0] = p[n-1][m/2][0] + x_sep[n-1]
                else:
                    p[n][m][0] = p[n-1][(m-1)/2][0] - x_sep[n-1]
                    plt.plot([p[n][m][0],p[n][m-1][0]],[p[n][m][1],p[n][m-1][1]],color='black',lw=lw)
                plt.plot([p[n][m][0],p[n][m][0]],[p[n][m][1],p[n][m][1]-y_sep[n]],color='black',lw=lw)

        draw_snip(-5,5,1820,10)
        draw_snip(p[-1][-1][0]-5,p[-1][0][0]+5,-1880,30)

    elif n_p == 3:
        y_sep = [0.,100.,100.,700.]
        x_sep = [20,10,5]
        p = [[[0.,0.] for m in range(2**n)] for n in range(4)]
        p[0][0][1] = 500.
        plt.plot([0,0],[2000,p[0][0][1]],color='black',lw=lw)
        for n in range(1,4):
            for m in range(2**n):
                p[n][m][1] = p[n-1][0][1] - y_sep[n-1]
                if m%2 == 0:
                    p[n][m][0] = p[n-1][m/2][0] + x_sep[n-1]
                else:
                    p[n][m][0] = p[n-1][(m-1)/2][0] - x_sep[n-1]
                    plt.plot([p[n][m][0],p[n][m-1][0]],[p[n][m][1],p[n][m-1][1]],color='black',lw=lw)
                plt.plot([p[n][m][0],p[n][m][0]],[p[n][m][1],p[n][m][1]-y_sep[n]],color='black',lw=lw)
                if n == 3:
                    plt.plot([p[n][m][0]],[p[n][m][1]-y_sep[n]],color='black',lw=lw,marker='o',mec='none',ms=3.5)

        draw_snip(-5,5,1820,10)

    plt.xlim(-40,40)
    plt.axis('off')

#ax = plt.subplot(259,sharey=ax1)
ax = plt.axes([3.5*axes_w,0.1*axes_h,axes_ws*3./2.,axes_hs],sharey=ax1)

y_sep = [0.,500.,500.,1000.]
x_sep = [20,10,5]
plt.arrow(-35, 1800, 0, -600, width=1, head_width=8, facecolor='black', head_length=100)
for k in range(3):
    p = [[[5*(k-1),0.] for m in range(2**n)] for n in range(4)]
    p[0][0][1] = 1000.
    plt.plot([5*(k-1),5*(k-1)],[2000,p[0][0][1]],color=c[k],lw=lw)
    for n in range(1,4):
        for m in range(2**n):
            if m%2 == 0:
                p[n][m+1][1] = p[n][m][1] = p[n-1][0][1] - y_sep[n-1] + 200*np.random.randn()
                p[n][m][0] = p[n-1][m/2][0] + x_sep[n-1]
                plt.plot([p[n-1][m/2][0],p[n-1][m/2][0]],[p[n][m][1],p[n-1][m/2][1]],color=c[k],lw=lw)
            else:
                p[n][m][0] = p[n-1][(m-1)/2][0] - x_sep[n-1]
                plt.plot([p[n][m][0],p[n][m-1][0]],[p[n][m][1],p[n][m-1][1]],color=c[k],lw=lw)
            if n == 3:
                lm = y_sep[n] + 200*np.random.randn()
                plt.plot([p[n][m][0],p[n][m][0]],[p[n][m][1],p[n][m][1]-lm],color=c[k],lw=lw)
                plt.plot([p[n][m][0]],[p[n][m][1]-lm],color=c[k],lw=lw,marker='o',mec='none',ms=3.5)

draw_snip(-10,10,1820,15)
plt.xlim(-45,45)
plt.axis('off')

files_summed = glob.glob('data/pots_pop_sum_[1-9]*')
files = glob.glob('../pyLaminaris/pots_pop_[1-9]*')
pots = np.concatenate([np.load(f)['pots'] for f in files[:10]],axis=1)
print pots.shape
pots_sum = np.sum([np.load(f)['pots'] for f in files_summed], axis=0)
pots_sum -= pots_sum[:,1000:].mean(axis=1,keepdims=True)
def pulse(t):
    return 2*(0.1
            + 0.9 * np.exp(-((t - 10.)/1.) ** 2))
n_electrodes = pots_sum.shape[0]
n_neurons = pots.shape[1]

fname_poulation = "/tmp/fig1_population_pulse.npz"
try:
    fh = np.load(fname_poulation)
    ret = fh['ret']
    ret2 = fh['ret2']
except:
    ret = np.zeros((n_electrodes,int(20./0.0025)+1))
    ret2 = np.zeros((n_electrodes,int(20./0.0025)+1))
    for n in range(n_electrodes):
        ret[n,:] = np.convolve(pots_sum[n,:],pulse(t3-1.25)*0.0025,mode='same')

    n_reps = 200
    for rep in range(n_reps):
        print rep
        for n_neuron in range(n_neurons):
            for t in utils.inhom_poisson(pulse,20.,0.,6.):
                t_ind = int((t)/0.0025)
                l = min(1000,ret.shape[1]-t_ind)
                if l>0: ret2[:,t_ind:t_ind+l] += pots[:,n_neuron,500:500+l]/n_reps
    print pots.shape
    np.savez_compressed(fname_poulation, ret=ret, ret2=ret2)

#ax4 = plt.subplot(2,5,10,sharey=ax1)
ax4 = plt.axes([5*axes_w,0.1*axes_h,axes_ws*2.,axes_hs],sharey=ax1)

for n in range(88,120,4):
    plt.plot(np.arange(ret.shape[1])*0.0025-10.,ret2[n,:]/(scale4)-(n-100)*100.,color='gray')
    plt.plot(np.arange(ret.shape[1])*0.0025-10.,ret[n,:]/(scale4)-(n-100)*100.,color='black')
plt.xlim(-5,5)
plt.axis('off')

times = [utils.inhom_poisson(pulse,20.,0.,6.)-10. for n in range(3)]
ax4.eventplot(times, colors=c, lineoffsets=(2000.-160.*np.arange(1,4)),
              linelengths=[150,150,150])

ttimes = np.arange(ret.shape[1])*0.0025-10.
plt.plot(ttimes,160.*3./2.*pulse(ttimes+10)+2000.-4*160,color='gray')

add_scalebar(ax4,sizex=5,sizey=4e5/(scale4),matchx=False,matchy=False,labelx='5 ms',
        labely='0.4 mV',loc=8,bbox_to_anchor=(220.5,20.0))


plt.ylim(-2000,2100)

plt.figtext(0.10, 0.95, 'A', fontsize=subfig_fontsize)
plt.figtext(0.40, 0.95, 'B', fontsize=subfig_fontsize)
plt.figtext(0.65, 0.95, 'C', fontsize=subfig_fontsize)
plt.figtext(0.10, 0.48, 'D', fontsize=subfig_fontsize)
plt.figtext(0.43, 0.48, 'E', fontsize=subfig_fontsize)
#plt.gcf().set_size_inches(4.48,4.45)
plt.gcf().set_size_inches(4.48,4.45*1.2)
plt.savefig('figs/fig_1.pdf')
#plt.show()
