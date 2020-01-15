import numpy as np
from scipy.integrate import odeint

from model.name2idx import parameters as C
from model.name2idx import variables as V
from model.param_const import f_params
from model.initial_condition import initial_values
from model.differential_equation import diffeq


class Simulation(object):
    t_start = 0
    t_end = 600
    h = 10000
    t = np.linspace(t_start,t_end,h)
    conditions = 12

    x = f_params()
    y0 = initial_values()
    
    for i in range(conditions):
        if i==0: 
            x[C.gene_turn] = x[C.Ski_turn]
            x[C.gene_act1] = x[C.Ski_act1]
            x[C.gene_act2] = x[C.Ski_act2]
            x[C.gene_act3] = x[C.Ski_act3]
            x[C.gene_inh1] = x[C.Ski_inh1]
            x[C.gene_inh2] = x[C.Ski_inh2]
            x[C.gene_inh3] = x[C.Ski_inh3]
        
            Y = odeint(diffeq,y0,t,args=tuple(x))
            Ski_treated =  np.log2(Y[:,V.gene])
        if i==1:
            x[C.gene_turn] = x[C.Skil_turn]
            x[C.gene_act1] = x[C.Skil_act1]
            x[C.gene_act2] = x[C.Skil_act2]
            x[C.gene_act3] = x[C.Skil_act3]
            x[C.gene_inh1] = x[C.Skil_inh1]
            x[C.gene_inh2] = x[C.Skil_inh2]
            x[C.gene_inh3] = x[C.Skil_inh3]
        
        
            Y = odeint(diffeq,y0,t,args=tuple(x))
            Skil_treated =  np.log2(Y[:,V.gene])

        if i==2:
            x[C.gene_turn] = x[C.Dnmt3a_turn]
            x[C.gene_act1] = x[C.Dnmt3a_act1]
            x[C.gene_act2] = x[C.Dnmt3a_act2]
            x[C.gene_act3] = x[C.Dnmt3a_act3]
            x[C.gene_inh1] = x[C.Dnmt3a_inh1]
            x[C.gene_inh2] = x[C.Dnmt3a_inh2]
            x[C.gene_inh3] = x[C.Dnmt3a_inh3]

            Y = odeint(diffeq,y0,t,args=tuple(x))
            Dnmt3a_treated =  np.log2(Y[:,V.gene])

        if i==3:
            x[C.gene_turn] = x[C.Sox4_turn]
            x[C.gene_act1] = x[C.Sox4_act1]
            x[C.gene_act2] = x[C.Sox4_act2]
            x[C.gene_act3] = x[C.Sox4_act3]
            x[C.gene_inh1] = x[C.Sox4_inh1]
            x[C.gene_inh2] = x[C.Sox4_inh2]
            x[C.gene_inh3] = x[C.Sox4_inh3]
        
            Y = odeint(diffeq,y0,t,args=tuple(x))
            Sox4_treated =  np.log2(Y[:,V.gene])

        if i==4:
            x[C.gene_turn] = x[C.Jun_turn]
            x[C.gene_act1] = x[C.Jun_act1]
            x[C.gene_act2] = x[C.Jun_act2]
            x[C.gene_act3] = x[C.Jun_act3]
            x[C.gene_inh1] = x[C.Jun_inh1]
            x[C.gene_inh2] = x[C.Jun_inh2]
            x[C.gene_inh3] = x[C.Jun_inh3]
        
            Y = odeint(diffeq,y0,t,args=tuple(x))
            Jun_treated =  np.log2(Y[:,V.gene])

        if i==5:
            x[C.gene_turn] = x[C.Smad7_turn]
            x[C.gene_act1] = x[C.Smad7_act1]
            x[C.gene_act2] = x[C.Smad7_act2]
            x[C.gene_act3] = x[C.Smad7_act3]
            x[C.gene_inh1] = x[C.Smad7_inh1]
            x[C.gene_inh2] = x[C.Smad7_inh2]
            x[C.gene_inh3] = x[C.Smad7_inh3]
        
            Y = odeint(diffeq,y0,t,args=tuple(x))
            Smad7_treated =  np.log2(Y[:,V.gene])

        if i==6:
            x[C.gene_turn] = x[C.Klf10_turn]
            x[C.gene_act1] = x[C.Klf10_act1]
            x[C.gene_act2] = x[C.Klf10_act2]
            x[C.gene_act3] = x[C.Klf10_act3]
            x[C.gene_inh1] = x[C.Klf10_inh1]
            x[C.gene_inh2] = x[C.Klf10_inh2]
            x[C.gene_inh3] = x[C.Klf10_inh3]
        
            Y = odeint(diffeq,y0,t,args=tuple(x))
            Klf10_treated =  np.log2(Y[:,V.gene])

        if i==7:
            x[C.gene_turn] = x[C.Bmp4_turn]
            x[C.gene_act1] = x[C.Bmp4_act1]
            x[C.gene_act2] = x[C.Bmp4_act2]
            x[C.gene_act3] = x[C.Bmp4_act3]
            x[C.gene_inh1] = x[C.Bmp4_inh1]
            x[C.gene_inh2] = x[C.Bmp4_inh2]
            x[C.gene_inh3] = x[C.Bmp4_inh3]
        
            Y = odeint(diffeq,y0,t,args=tuple(x))
            Bmp4_treated =  np.log2(Y[:,V.gene])

        if i==8:
            x[C.gene_turn] = x[C.Cxcl15_turn]
            x[C.gene_act1] = x[C.Cxcl15_act1]
            x[C.gene_act2] = x[C.Cxcl15_act2]
            x[C.gene_act3] = x[C.Cxcl15_act3]
            x[C.gene_inh1] = x[C.Cxcl15_inh1]
            x[C.gene_inh2] = x[C.Cxcl15_inh2]
            x[C.gene_inh3] = x[C.Cxcl15_inh3]
        
            Y = odeint(diffeq,y0,t,args=tuple(x))
            Cxcl15_treated =  np.log2(Y[:,V.gene])

        if i==9:
            x[C.gene_turn] = x[C.Dusp5_turn]
            x[C.gene_act1] = x[C.Dusp5_act1]
            x[C.gene_act2] = x[C.Dusp5_act2]
            x[C.gene_act3] = x[C.Dusp5_act3]
            x[C.gene_inh1] = x[C.Dusp5_inh1]
            x[C.gene_inh2] = x[C.Dusp5_inh2]
            x[C.gene_inh3] = x[C.Dusp5_inh3]
        
            Y = odeint(diffeq,y0,t,args=tuple(x))
            Dusp5_treated =  np.log2(Y[:,V.gene])

        if i==10:
            x[C.gene_turn] = x[C.Tgfa_turn]
            x[C.gene_act1] = x[C.Tgfa_act1]
            x[C.gene_act2] = x[C.Tgfa_act2]
            x[C.gene_act3] = x[C.Tgfa_act3]
            x[C.gene_inh1] = x[C.Tgfa_inh1]
            x[C.gene_inh2] = x[C.Tgfa_inh2]
            x[C.gene_inh3] = x[C.Tgfa_inh3]
        
            Y = odeint(diffeq,y0,t,args=tuple(x))
            Tgfa_treated =  np.log2(Y[:,V.gene])

        if i==11:
            x[C.gene_turn] = x[C.Pdk4_turn]
            x[C.gene_act1] = x[C.Pdk4_act1]
            x[C.gene_act2] = x[C.Pdk4_act2]
            x[C.gene_act3] = x[C.Pdk4_act3]
            x[C.gene_inh1] = x[C.Pdk4_inh1]
            x[C.gene_inh2] = x[C.Pdk4_inh2]
            x[C.gene_inh3] = x[C.Pdk4_inh3]
        
            Y = odeint(diffeq,y0,t,args=tuple(x))
            Pdk4_treated =  np.log2(Y[:,V.gene])