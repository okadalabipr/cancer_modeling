import numpy as np
from scipy.integrate import odeint

from model.name2idx import parameters as C
from model.name2idx import variables as V
from model.param_const import f_params
from model.initial_condition import initial_values
from model.differential_equation import diffeq


class Simulation(object):
    
    tspan_ss = range(3600*100+1)  
    tspan_a = range(3601)         
    tspan_b = range(3600*6+1)     
    
    t = np.arange(3600*7+1)/3600.
    
    x = f_params()
    y0 = initial_values()
    
    # t < 0
    Yss = odeint(diffeq,y0,tspan_ss,args=tuple(x))
    y0 = Yss[-1,:]
    
    # 0 <= t < 1
    Ya = odeint(diffeq,y0,tspan_a,args=tuple(x))
    y0 = Ya[-1,:]
    x[C.TR] = 1
    
    # 1 <= t <= 7
    Yb = odeint(diffeq,y0,tspan_b,args=tuple(x))
    
    Y = np.vstack((np.delete(Ya,-1,axis=0),Yb))
    
    Neutral_IKK       = Y[:,V.IKKn] 
    Active_IKK        = Y[:,V.IKKa] 
    Inactive_IKK      = Y[:,V.IKKi] 
    Free_cyt_IkBa     = Y[:,V.IkBa] 
    Cyt               = Y[:,V.IkBaNFkB] 
    Free_nuclear_IkBa = Y[:,V.IkBan] 
    Free_nuclear_NFkB = Y[:,V.NFkBn] 
    IkBa_mRNA         = Y[:,V.IkBat] 
    A20_mRNA          = Y[:,V.A20t] 
    A20_protein       = Y[:,V.A20] 
    cgen_mRNA         = Y[:,V.cgent] 
        
        