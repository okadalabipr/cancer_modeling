import numpy as np
from scipy.integrate import odeint

from .name2idx import C, V
from .set_model import diffeq, param_values, initial_values

class Simulation(object):
    x = param_values()
    y0 = initial_values()

    tspan = range(1200)
    t = np.array(tspan)/60

    Y = odeint(diffeq,y0,tspan,args=tuple(x))

    CycA = Y[:,V.tCa]
    CycE = Y[:,V.tCe]
    active_RC = Y[:,V.aRc]
    P21_tot = Y[:,V.tP21]