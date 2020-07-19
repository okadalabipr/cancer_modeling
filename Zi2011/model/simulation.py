import numpy as np
from scipy.integrate import odeint

from .name2idx import V
from .set_model import diffeq, param_values, initial_values


class Simulation(object):
    tspan = np.linspace(0,480,4801)
    t = np.array(tspan)/60  # min -> hour
    Ton = np.linspace(0,0.5,6)  # 30 s pulse 
    Toff = np.linspace(0,479.5,4796)
    
    x = param_values()
    y0 = initial_values() 
            
    Y = odeint(diffeq,y0,tspan,args=tuple(x))

    totalNumPSmad2_sustained = (Y[:,V.PSmad2c] + 2*Y[:,V.PSmad2_PSmad2_c] + Y[:,V.PSmad2_PSmad4_c])*2.3*602 \
                                + (Y[:,V.PSmad2n] + 2*Y[:,V.PSmad2_PSmad2_n] + Y[:,V.PSmad2_Smad4_n])*602
                            
    pulse = odeint(diffeq,y0,Ton,args=tuple(x))
    Y0 = pulse[-1,:]
    # washout
    Y0[V.TGF_beta_ex] = 0
    washout = odeint(diffeq,Y0,Toff,args=tuple(x))
    
    Y = np.vstack((np.delete(pulse,-1,axis=0),washout))
    totalNumPSmad2_singlePulse = (Y[:,V.PSmad2c] + 2*Y[:,V.PSmad2_PSmad2_c] + Y[:,V.PSmad2_PSmad4_c])*2.3*602 \
                                    + (Y[:,V.PSmad2n] + 2*Y[:,V.PSmad2_PSmad2_n] + Y[:,V.PSmad2_Smad4_n])*602