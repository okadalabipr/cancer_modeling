import numpy as np
from scipy.integrate import odeint

from model.set_model import *

class Simulation(object):
    x = f_params()
    y0 = initial_values()

    tspan = range(1200)
    t = np.array(tspan)/60

    Y = odeint(diffeq,y0,tspan,args=tuple(x))

    CycA = Y[:,V.tCa]
    CycE = Y[:,V.tCe]
    active_RC = Y[:,V.aRc]
    P21_tot = Y[:,V.tP21]