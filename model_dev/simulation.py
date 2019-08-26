import numpy as np
from scipy.integrate import odeint

from model.name2idx import f_parameter as C
from model.name2idx import f_variable as V
from model.param_const import f_params
from model.initial_condition import initial_values
from model.differential_equation import diffeq


class Simulation(object):
    """
    This is where you define the simulations you want to run. In this file you 
    can define different conditions for each simulation 
    (for example, ligand concentration) and how you would like each variable to 
    be simulated (i.e. do you want absolute concentration to be simulated? or 
    percentage change over time? Etc).
    """
