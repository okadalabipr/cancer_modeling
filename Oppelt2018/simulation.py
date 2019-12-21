import numpy as np
from scipy.integrate import odeint

from model.name2idx import parameters as C
from model.name2idx import variables as V
from model.param_const import f_params_noDCF, f_params_DCF
from model.initial_condition import initial_values
from model.differential_equation import diffeq

class Simulation(object):
    tspan = range(201)
    t = np.array(tspan)
    condition = 2

    nuclear_IkBa = np.empty((len(t),condition))
    nuclear_NFKB = np.empty((len(t),condition))

    y0 = initial_values()
    for i in range(condition):
        if i==0:
            x = f_params_noDCF()
        elif i==1:
            x = f_params_DCF()

        Y = odeint(diffeq,y0,tspan,args=tuple(x))

        nuclear_IkBa[:,i] = x[C.Vnuc]*(Y[:,V.nNfkIkb] + Y[:,V.nIkb])
        nuclear_NFKB[:,i] = x[C.Vnuc]*(Y[:,V.pnNfk] + Y[:,V.nNfk] + Y[:,V.nNfkIkb])