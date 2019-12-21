import numpy as np
from scipy.integrate import odeint

from model.name2idx import parameters as C
from model.name2idx import variables as V
from model.param_const import f_params
from model.initial_condition import initial_values
from model.differential_equation import diffeq


class Simulation(object):
    tspan = range(121)
    t = np.array(tspan)
    
    condition = 4
    
    IL13stimulation = np.empty((len(t),condition))
    Rec             = np.empty((len(t),condition))
    Rec_i           = np.empty((len(t),condition))
    IL13_Rec        = np.empty((len(t),condition))
    p_IL13_Rec      = np.empty((len(t),condition))
    p_IL13_Rec_i    = np.empty((len(t),condition))
    JAK2            = np.empty((len(t),condition))
    pJAK2           = np.empty((len(t),condition))
    SHP1            = np.empty((len(t),condition))
    STAT5           = np.empty((len(t),condition))
    pSTAT5          = np.empty((len(t),condition))
    SOCS3mRNA       = np.empty((len(t),condition))
    DecoyR          = np.empty((len(t),condition))
    IL13_DecoyR     = np.empty((len(t),condition))
    SOCS3           = np.empty((len(t),condition))
    CD274mRNA       = np.empty((len(t),condition))
    
    x = f_params()
    y0 = initial_values()
    
    for i in range(condition):
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