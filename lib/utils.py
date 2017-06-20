import numpy as _np


def hom_poisson(rate, t_end=1., t_start=0., t_ref=0.0):
    '''
    Generate a poisson event train at a fixed rate in a given time window

    homogeneous Poisson process

    A homogeneous Poisson process generates events (spikes) with a constant 
    probability or rate r(t) = r. Spikes are independent. Thus, at each 
    time point t, the probability P of observing a spike within 
    a sufficiently small temporal window from t to t + delta_t is 
    P= r*delta_t.

    There are two simple ways of implementing a homogeneous Poisson process:
    1.    Progress through time in small steps of size delta_t, 
          draw a random number x (from a uniform distribution 
          between 0 and 1, Matlab function 'rand' 
          at each time step. If x < P, generate a spike.

    2.    Generate interspike intervals from an exponential probability 
          density. When x is uniformly distributed between 0 and 1, 
          its negative logarithm is exponentially distributed. Thus, we 
          can generate spike times t(i) iteratively from the 
          formula t(i+1) = t(i) - log(x)/r.

    Using implementation #2
    '''
    t = t_start
    train = []
    while t < t_end:
        ISI = -_np.log(_np.random.random()) / rate  # ISIs in seconds
        t = t + ISI
        train.append(t)
        t = t + t_ref

    return _np.array(train)


def inhom_poisson(rate, t_end=1., t_start=0., rate_max=1000., t_ref=0.0):
    '''
    # inhomogeneous Poisson process

    An inhomogeneous Poisson process is characterized by a time-dependent
    rate r(t). There are several ways of generating spikes.
    Two basic ways are:
    1.    Progress through time in small intervals of width delta_t.
          For sufficiently small delta_t, the probability P(i) of
          observing a spike in interval i from t(i) = i*delta_t to
          t_(i) + delta_t is then given by
              P(i) = integral_t(i)^[t_(i)+delta_t)] r(tau) d tau .
          Then, draw a random number x(i) from a uniform distribution
          for each time interval. If x(i) < P(i)$, generate a spike.

    2.    'Thinning' the spike train of a homogeneous Poisson process:
          First, a spike sequence is generated with a homogeneous 
          Poisson process at rate r_max = max[r(t)]. The spike 
          sequence is then thinned by generating a random number 
          x(i) for each spike and removing the spike at time 
          t(i) from the train if r(t(i))/r_max < x(i).

    Here Method #2 is used.
    '''
    train = hom_poisson(rate_max, t_end, t_start)
    train_start = hom_poisson(rate(t_start), t_end, t_start)
    # thin the spike train

    train_thinned = [train_start[0]]
    for n, t in enumerate(train):
        if (t - train_thinned[-1] >= t_ref
            and _np.random.random() < rate(t) / rate_max):
            train_thinned.append(t)

    return _np.array(train_thinned)
