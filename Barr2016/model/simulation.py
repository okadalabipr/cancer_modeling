import numpy as np
from scipy.integrate import odeint

from .name2idx import C, V
from model.set_model import diffeq, param_values, initial_values

class Simulation(object):
    x = param_values()
    y0 = initial_values()

    tspan = range(901)
    t = np.array(tspan)

    Y = odeint(diffeq,y0,tspan,args=tuple(x))

    CyclinA = Y[:,V.CycAT]-Y[:,V.CycAp27]
    CyclinE = Y[:,V.CycET]-Y[:,V.CycEp27]
    p27_tot = Y[:,V.p27T]
