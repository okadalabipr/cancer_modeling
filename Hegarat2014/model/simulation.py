import numpy as np
from scipy.integrate import odeint

from .name2idx import C, V
from .set_model import diffeq, param_values, initial_values


class Simulation(object):
    tspan = [i/10 for i in range(120*10+1)]
    t = np.array(tspan)
    
    condition = 9
    
    Gwl = np.empty((len(t),condition))
    Cdc25 = np.empty((len(t),condition))
    ENSAP = np.empty((len(t),condition))
    Y15 = np.empty((len(t),condition))
    B55 = np.empty((len(t),condition))
    
    x = param_values()
    y0 = initial_values()
    
    for i in range(condition):
        #OA insensitive phosphatase
        if i in [0,3,6]:
            x[C.kigwl] = 0
            x[C.kigwl_d] = 2
            x[C.kigwl_dd] = 0
        #OA sensitive phosphatase
        if i in [1,4,7]:
            x[C.kigwl] = 0
            x[C.kigwl_d] = 0.02
            x[C.kigwl_dd] = 2
        #PP2A-B55
        if i in [2,5,8]:
            x[C.kigwl] = 2
            x[C.kigwl_d] = 0.02
            x[C.kigwl_dd] = 0
        
        #Cdk1 Inhibition +OA
        if i in [3,4,5]:
            x[C.OA] = 100
            x[C.RO] = 25
            
        #Mitotic block
        if i in [6,7,8]:
            y0[V.MPF] = 0.96
            y0[V.Cdc25] = 0.97
            y0[V.Wee1] = 0.03
            y0[V.Gwl] = 0.9
            y0[V.ENSAPt] = 0.75
            y0[V.PP2] = 0.027
            
            x[C.OA] = 0
            x[C.RO] = 100
            
        Y = odeint(diffeq,y0,tspan,args=tuple(x))
        Gwl[:,i] = Y[:,V.Gwl]
        Cdc25[:,i] = Y[:,V.Cdc25]
        ENSAP[:,i] = Y[:,V.ENSAPt]
        B55[:,i] = Y[:,V.PP2]
        Y15[:,i] = x[C.CycT] - Y[:,V.MPF]