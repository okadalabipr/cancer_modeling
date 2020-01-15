import numpy as np
from scipy.integrate import odeint

from model.name2idx import parameters as C
from model.name2idx import variables as V
from model.param_const import f_params
from model.initial_condition import initial_values
from model.differential_equation import diffeq

class Simulation(object):
    
    def get_steady_state():
        x = f_params()
        y0 = initial_values()
        
        ss_time = range(2401)  # 2400 min
        y0[V.Ins] = 0.01  # 0.01 nM of insulin during starvation
        
        Y = odeint(diffeq, y0, ss_time, args=tuple(x))
        
        return Y[-1,:]
        
        
    tspan = range(481)
    t = np.array(tspan)
    
    condition = 5

    pAKT   = np.empty((len(t), condition))
    pS6K   = np.empty((len(t), condition))
    pGSK3B = np.empty((len(t), condition))
    G6Pase = np.empty((len(t), condition))

    x = f_params()
    y0 = get_steady_state()
    
    for i in range(condition):
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
