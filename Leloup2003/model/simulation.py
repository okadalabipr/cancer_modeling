import numpy as np
from scipy.integrate import odeint

from .set_model import diffeq, param_values, initial_values

class Simulation(object):
    x = param_values()
    y0 = initial_values()

    tspan = np.arange(0,72,0.01)
    t = np.array(tspan)

    Y = odeint(diffeq, y0, tspan, args=tuple(x))