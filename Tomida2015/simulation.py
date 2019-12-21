import numpy as np
from scipy.integrate import odeint

from model.name2idx import parameters as C
from model.name2idx import variables as V
from model.param_const import f_params
from model.initial_condition import initial_values
from model.differential_equation import diffeq

class Simulation(object):
    x = f_params()
    y0 = initial_values()

    t = range(481)

    condition = 4

    p38_activity = np.empty((len(t),condition))

    for i in range(condition):
        # k8: the rate constant for MKP-1 protein degradation
        if i==0:
            x[C.k8] = 0.024
        elif i==1:
            x[C.k8] = 0.012
        elif i==2:
            x[C.k8] = 0.008
        elif i==3:
            x[C.k8] = 0.004

        Y = odeint(diffeq,y0,t,args=tuple(x))

        p38_activity[:,i] = Y[:,V.FRET]