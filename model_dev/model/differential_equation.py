import numpy as np
from .name2idx import f_parameter as C
from .name2idx import f_variable as V

def diffeq(y,t,*x):
    dydt = [0]*V.len_f_vars
    """
    This file contains the differential equations that instruct the model how to
    change concentrations of reactants over the time course of the simulation.
    """
    return dydt