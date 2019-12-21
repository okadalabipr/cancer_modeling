import numpy as np
from scipy.integrate import odeint

from model.name2idx import parameters as C
from model.name2idx import variables as V
from model.param_const import f_params
from model.initial_condition import initial_values
from model.differential_equation import diffeq

class Simulation(object):
    t = range(121)
    condition = 3

    totalShc = np.empty((len(t),condition))
    totalGrb2 = np.empty((len(t),condition))
    RSh = np.empty((len(t),condition))
    RGrb2 = np.empty((len(t),condition))
    totalSOS = np.empty((len(t),condition))
    ShGS = np.empty((len(t),condition))
    PLCg = np.empty((len(t),condition))

    x = f_params()
    y0 = initial_values()

    for i in range(condition):
        if i==0: # 20nM
            pass
        elif i==1: # 2nM
            y0[V.EGF] = 68.
        elif i==2: # Absence of the PLCγP translocation step
            y0[V.EGF] = 680.
            x[C.k25f] = 0.
            x[C.k25b] = 0.

        Y = odeint(diffeq,y0,t,args=tuple(x))

        totalShc[:,i] = Y[:,V.R_ShP]+Y[:,V.R_Sh_G]+Y[:,V.R_Sh_G_S]+Y[:,V.ShP]+Y[:,V.Sh_G]+Y[:,V.Sh_G_S]
        totalGrb2[:,i] = Y[:,V.R_Sh_G]+Y[:,V.Sh_G]+Y[:,V.R_Sh_G_S]+Y[:,V.Sh_G_S]
        RSh[:,i] = Y[:,V.R_ShP]+Y[:,V.R_Sh_G]+Y[:,V.R_Sh_G_S]
        RGrb2[:,i] = Y[:,V.R_G]+Y[:,V.R_G_S]+Y[:,V.R_Sh_G]+Y[:,V.R_Sh_G_S]
        totalSOS[:,i] = Y[:,V.R_G_S]+Y[:,V.R_Sh_G_S]
        ShGS[:,i] = Y[:,V.Sh_G_S]
        PLCg[:,i] = Y[:,V.R_PLP]+Y[:,V.PLCgP]