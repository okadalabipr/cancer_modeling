import numpy as np
from scipy.integrate import odeint

from .name2idx import C, V
from .set_model import (diffeq, param_values_noDCF, 
                        param_values_DCF, initial_values)


class Simulation(object):
    tspan = range(201)
    t = np.array(tspan)
    conditions = 2

    nuclear_IkBa = np.empty((len(t), conditions))
    nuclear_NFKB = np.empty((len(t), conditions))

    y0 = initial_values()
    for i in range(conditions):
        if i == 0:
            x = param_values_noDCF()
        elif i == 1:
            x = param_values_DCF()

        Y = odeint(diffeq, y0, tspan, args=tuple(x))

        nuclear_IkBa[:, i] = x[C.Vnuc]*(Y[:, V.nNfkIkb] + Y[:, V.nIkb])
        nuclear_NFKB[:, i] = x[C.Vnuc]*(Y[:, V.pnNfk] + Y[:, V.nNfk] + Y[:, V.nNfkIkb])