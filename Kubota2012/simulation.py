import numpy as np
from scipy.integrate import odeint

from model.name2idx import parameters as C
from model.name2idx import variables as V
from model.param_const import f_params
from model.initial_condition import initial_values
from model.differential_equation import diffeq

class Simulation(object):
    tspan = range(2400 + 481)
    t = np.arange(481)
    condition = 5

    pAKT   = np.empty((len(t), condition))
    pS6K   = np.empty((len(t), condition))
    pGSK3B = np.empty((len(t), condition))
    G6Pase = np.empty((len(t), condition))

    x = f_params()
    y0 = initial_values()
    
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
        
        pAKT[:, i] = Y[2400:, V.pAKT]
        pS6K[:, i] = Y[2400:, V.pS6K] * 83.8672192461257
        pGSK3B[:, i] = Y[2400:, V.pGSK3B] * 0.111097316860158
        G6Pase[:, i] = Y[2400:, V.G6Pase] * 0.0363622452066626
