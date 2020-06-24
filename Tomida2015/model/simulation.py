import numpy as np
from scipy.integrate import odeint

from .name2idx import C, V
from .set_model import diffeq, param_values, initial_values


class Simulation(object):
    x = param_values()
    y0 = initial_values()

    t = range(481)

    conditions = 4

    p38_activity = np.empty((len(t), conditions))

    for i in range(conditions):
        # k8: the rate constant for MKP-1 protein degradation
        if i == 0:
            x[C.k8] = 0.024
        elif i == 1:
            x[C.k8] = 0.012
        elif i == 2:
            x[C.k8] = 0.008
        elif i == 3:
            x[C.k8] = 0.004

        Y = odeint(diffeq, y0, t, args=tuple(x))

        p38_activity[:, i] = Y[:, V.FRET]