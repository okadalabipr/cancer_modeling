import numpy as np
from scipy.integrate import odeint

from .name2idx import C, V
from .set_model import diffeq, param_values, initial_values

class Simulation(object):

    def _get_steady_state():
        x = param_values()
        y0 = initial_values()
        
        ss_time = range(2401)  # 2400 min
        y0[V.Ins] = 0.01  # 0.01 nM of insulin during starvation
        
        Y = odeint(diffeq, y0, ss_time, args=tuple(x))
        
        return Y[-1,:]
        
        
    tspan = range(481)
    t = np.array(tspan)
    
    conditions = 5

    pAKT   = np.empty((len(t), conditions))
    pS6K   = np.empty((len(t), conditions))
    pGSK3B = np.empty((len(t), conditions))
    G6Pase = np.empty((len(t), conditions))

    x = param_values()
    y0 = _get_steady_state()
    
    for i in range(conditions):
        if i == 0:
            y0[V.Ins] = 0.01
        elif i == 1:
            y0[V.Ins] = 0.03
        elif i == 2:
            y0[V.Ins] = 0.1
        elif i == 3:
            y0[V.Ins] = 0.3
        elif i == 4:
            y0[V.Ins] = 1.0

        Y = odeint(diffeq, y0, tspan, args=tuple(x))
        
        pAKT[:, i] = Y[:, V.pAKT]
        pS6K[:, i] = Y[:, V.pS6K] * 83.8672192461257
        pGSK3B[:, i] = Y[:, V.pGSK3B] * 0.111097316860158
        G6Pase[:, i] = Y[:, V.G6Pase] * 0.0363622452066626
