import numpy as np
from scipy.integrate import odeint

from .name2idx import C, V
from .set_model import diffeq, param_values, initial_values


class Simulation(object):
    tspan = range(121)
    t = np.array(tspan)
    
    conditions = 4
    
    IL13stimulation = np.empty((len(t),conditions))
    Rec             = np.empty((len(t),conditions))
    Rec_i           = np.empty((len(t),conditions))
    IL13_Rec        = np.empty((len(t),conditions))
    p_IL13_Rec      = np.empty((len(t),conditions))
    p_IL13_Rec_i    = np.empty((len(t),conditions))
    JAK2            = np.empty((len(t),conditions))
    pJAK2           = np.empty((len(t),conditions))
    SHP1            = np.empty((len(t),conditions))
    STAT5           = np.empty((len(t),conditions))
    pSTAT5          = np.empty((len(t),conditions))
    SOCS3mRNA       = np.empty((len(t),conditions))
    DecoyR          = np.empty((len(t),conditions))
    IL13_DecoyR     = np.empty((len(t),conditions))
    SOCS3           = np.empty((len(t),conditions))
    CD274mRNA       = np.empty((len(t),conditions))
    
    x = param_values()
    y0 = initial_values()
    
    for i in range(conditions):
        if i==0:
            y0[V.IL13stimulation] = 80.0
        elif i==1:
            y0[V.IL13stimulation] = 20.0
        elif i==2:
            y0[V.IL13stimulation] = 4.0
        elif i==3:
            y0[V.IL13stimulation] = 0.0
            
        Y = odeint(diffeq,y0,tspan,args=tuple(x))
        
        IL13stimulation[:,i] = Y[:,V.IL13stimulation]
        Rec[:,i] = Y[:,V.Rec]
        Rec_i[:,i] = Y[:,V.Rec_i]
        IL13_Rec[:,i] = Y[:,V.IL13_Rec]
        p_IL13_Rec[:,i] = Y[:,V.p_IL13_Rec]
        p_IL13_Rec_i[:,i] = Y[:,V.p_IL13_Rec_i]
        JAK2[:,i] = Y[:,V.JAK2]
        pJAK2[:,i] = Y[:,V.pJAK2]
        SHP1[:,i] = Y[:,V.SHP1]
        STAT5[:,i] = Y[:,V.STAT5]
        pSTAT5[:,i] = Y[:,V.pSTAT5]
        SOCS3mRNA[:,i] = Y[:,V.SOCS3mRNA]
        DecoyR[:,i] = Y[:,V.DecoyR]
        IL13_DecoyR[:,i] = Y[:,V.IL13_DecoyR]
        SOCS3[:,i] = Y[:,V.SOCS3]
        CD274mRNA[:,i] = Y[:,V.CD274mRNA]