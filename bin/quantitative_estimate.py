from brian2 import *
V_bar = 70*mV
r_L = 1000*ohm*mmetre
tau = 0.25*ms
v = 1.*metre/second
r = 100* umetre
a = 2*umeter
sigma = 0.33*siemens/meter
dx = 0.1*umeter
x = arange(-10*cm,10*cm,dx)
Vs = []
ts =  arange(-10*ms,10*ms,0.1*ms)
for t in ts:
    V = V_bar*exp(-((x/v-t)/tau)**2)
    d2Vdx2 = diff(diff(V))/(dx**2)
    i_m = a*d2Vdx2/(2*r_L)
    i_m_ring = i_m * 2*pi*a
    w = 1/sqrt(x**2+r**2)[1:-1]
    Vs.append(sum(w*i_m_ring*dx)/(4*pi*sigma))
    if abs(t/ms)<0.05:
        print Vs[-1]
Vs = np.array(Vs/volt)*volt
