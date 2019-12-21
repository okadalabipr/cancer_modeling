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

    tspan = range(901)
    t = np.array(tspan)

    Y = odeint(diffeq,y0,tspan,args=tuple(x))

    CyclinA = Y[:,V.CycAT]-Y[:,V.CycAp27]
    CyclinE = Y[:,V.CycET]-Y[:,V.CycEp27]
    p27_tot = Y[:,V.p27T]
