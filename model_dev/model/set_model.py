from .name2idx import C, V

def diffeq(y, t, *x):

    dydt = [0] * V.NUM
    """
    This file contains the differential equations that instruct the model how to
    change concentrations of reactants over the time course of the simulation.
    """
    return dydt


def param_values():

    x = [0] * C.NUM
    """
    This file contains the parameters used in the differential equations.
    """

    return x


def initial_values():

    y0 = [0] * V.NUM
    """
    This is where you define non-zero initial concentrations.
    """

    return y0