from brian2 import *
import numpy as np

V_bar = 70*mV
r_L = 1000*ohm*mmetre
tau = 0.25*ms
v = 1.*metre/second
r = 1000* umetre
a = 2*umeter
sigma = 0.33*siemens/meter
dx = 0.1*umeter
x = arange(-10*cm,10*cm,dx)
Vs = []
dps = []
qps = []
ts =  arange(-10*ms,10*ms,0.1*ms)
t = 0*second
rs = arange(50*umeter, 6*mmeter, 10*umeter)
n = np.ones(x.shape)
#n[x>(-30*umeter)] = 2.
n[x>(0*umeter)] = 2.

def symmetric_diff(inp):
    ret = np.zeros_like(inp)
    ret[1:] = np.diff(inp)/2
    ret[:-1] = np.diff(inp)/2
    ret[0] *= 2
    ret[-1] *= 2
    return ret

for t in ts:
    V = V_bar*exp(-((x/v-t)/tau)**2)
    d2Vdx2 = symmetric_diff(n*symmetric_diff(V))/(dx**2)
    i_m = a*d2Vdx2/(2*r_L)
    i_m_ring = i_m * 2*pi*a

    #for r in rs:
        #w = 1/sqrt(x**2+r**2)
    w = 1/sqrt((x-r)**2)
    Vs.append(sum(w*i_m_ring*dx)/(4*pi*sigma))
    dp = (sum(x*i_m_ring*dx)/(4*pi*sigma))
    qp = (sum((-x**2/2)*i_m_ring*dx)/(4*pi*sigma))
    dps.append(dp)
    qps.append(qp)
    #if abs(t/ms)<0.05:
    #    print Vs[-1]
    #    print dp[-1]/(r)**2
    #    print qp[-1]/(r)**3
#Vs = np.array(Vs/volt)*volt
#plot(rs,-Vs/uvolt,color='green')
#plot(rs,-dp/(rs**2)/uvolt,ls='dashed',color='k')
#plot(rs,-qp/(rs**3)/uvolt,ls='dashed',color='k')
#plot(rs,-(dp/(rs**2)+qp/(rs**3))/uvolt,color='blue')
#print 'Dipole:    ',dp/(uvolt*(mmeter)**2)
#print 'Quadrupole:',qp/(uvolt*(mmeter)**3)
#loglog()
#show()
print min(dps)/(volt*meter*meter)
print max(dps)/(volt*meter*meter)
