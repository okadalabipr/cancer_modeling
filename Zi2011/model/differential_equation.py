import numpy as np
from .name2idx import parameters as C
from .name2idx import variables as V

def diffeq(y,t,*x):
    dydt = [0]*V.len_f_vars
    
            
    totalNuclearPSmad2 = y[V.PSmad2n] + 2*y[V.PSmad2_PSmad2_n] + y[V.PSmad2_Smad4_n]
    totalNumPSmad2 = (y[V.PSmad2c] + 2*y[V.PSmad2_PSmad2_c] + y[V.PSmad2_PSmad4_c])*2.3*602 \
                     + (y[V.PSmad2n] + 2*y[V.PSmad2_PSmad2_n] + y[V.PSmad2_Smad4_n])*602
    totalNuclearSmad2 = y[V.Smad2n] + y[V.PSmad2n] + 2*y[V.PSmad2_PSmad2_n] + y[V.PSmad2_Smad4_n]
    koff_ns = x[C.kon_ns]*x[C.KD_ns]
    Vcyt = 2.3e-12
    Vnuc = 1e-12
    Vmed = 0.002/(1e6*np.exp(np.log(1.45)*t/1440))
    '''
    Vmed_10mL = 0.010/(1e6*np.exp(np.log(1.45)*t/1440))
    TGF_beta_dose = y[V.TGF_beta_ex]*1e-9*Vmed*6e23
    TGF_beta_dose_10mL = y[V.TGF_beta_ex]*1e-9*Vmed_10mL*6e23
    '''

    dydt[V.TGF_beta_ex] = -Vcyt*x[C.ka_LRC]*y[V.TGF_beta_ex]*y[V.T2R_surf]*y[V.T1R_surf]/Vmed \
                          - x[C.kon_ns]*y[V.TGF_beta_ex] + koff_ns*y[V.TGF_beta_ns]
                          
    dydt[V.T1R_surf] = x[C.kprod_T1R] - x[C.ki]*y[V.T1R_surf] + x[C.kr]*y[V.T1R_endo] \
                       - x[C.ka_LRC]*y[V.TGF_beta_ex]*y[V.T2R_surf]*y[V.T1R_surf]
                       
    dydt[V.T1R_endo] = x[C.ki]*y[V.T1R_surf] - x[C.kr]*y[V.T1R_endo] - x[C.kdeg_T1R]*y[V.T1R_endo] \
                       + x[C.kdiss_LRC]*y[V.LRC_endo]

    dydt[V.T2R_surf] = x[C.kprod_T2R] - x[C.ki]*y[V.T2R_surf] + x[C.kr]*y[V.T2R_endo] \
                       - x[C.ka_LRC]*y[V.TGF_beta_ex]*y[V.T2R_surf]*y[V.T1R_surf]
                      
    dydt[V.T2R_endo] = x[C.ki]*y[V.T2R_surf] - x[C.kr]*y[V.T2R_endo] - x[C.kdeg_T2R]*y[V.T2R_endo] \
                       + x[C.kdiss_LRC]*y[V.LRC_endo]
                      
    dydt[V.LRC_surf] = x[C.ka_LRC]*y[V.TGF_beta_ex]*y[V.T2R_surf]*y[V.T1R_surf] - x[C.ki]*y[V.LRC_surf] \
                       - x[C.klid]*y[V.LRC_surf]*totalNuclearPSmad2
                       
    dydt[V.LRC_endo] = x[C.ki]*y[V.LRC_surf] - x[C.kdiss_LRC]*y[V.LRC_endo] - x[C.kdeg_LRC]*y[V.LRC_endo]
    
    dydt[V.Smad2c] = Vnuc*x[C.kexp_Smad2]*y[V.Smad2n]/Vcyt - x[C.kpho_Smad2]*y[V.Smad2c]*y[V.LRC_endo] \
                     - x[C.kimp_Smad2]*y[V.Smad2c]
                     
    dydt[V.Smad2n] = Vcyt*x[C.kimp_Smad2]*y[V.Smad2c]/Vnuc - x[C.kexp_Smad2]*y[V.Smad2n] + x[C.kdepho_Smad2]*y[V.PSmad2n]
                     
    dydt[V.Smad4c] = Vnuc*x[C.kexp_Smad4]*y[V.Smad4n]/Vcyt - x[C.kon_Smads]*y[V.PSmad2c]*y[V.Smad4c] \
                     + x[C.koff_Smads]*y[V.PSmad2_PSmad4_c] - x[C.kimp_Smad4]*y[V.Smad4c]
                     
    dydt[V.Smad4n] = Vcyt*x[C.kimp_Smad4]*y[V.Smad4c]/Vnuc - x[C.kexp_Smad4]*y[V.Smad4n] \
                     + x[C.koff_Smads]*y[V.PSmad2_Smad4_n] - x[C.kon_Smads]*y[V.PSmad2n]*y[V.Smad4n]
                     
    dydt[V.PSmad2c] = x[C.kpho_Smad2]*y[V.Smad2c]*y[V.LRC_endo] - x[C.kimp_Smad2]*y[V.PSmad2c] \
                      + Vnuc*x[C.kexp_Smad2]*y[V.PSmad2n]/Vcyt - x[C.kon_Smads]*y[V.PSmad2c]*y[V.Smad4c] \
                      + x[C.koff_Smads]*y[V.PSmad2_PSmad4_c] - 2*x[C.kon_Smads]*y[V.PSmad2c]*y[V.PSmad2c] \
                      + 2*x[C.koff_Smads]*y[V.PSmad2_PSmad2_c]
                      
    dydt[V.PSmad2_PSmad2_c] = x[C.kon_Smads]*y[V.PSmad2c]*y[V.PSmad2c] - x[C.koff_Smads]*y[V.PSmad2_PSmad2_c] \
                              - x[C.kimp_Smads]*y[V.PSmad2_PSmad2_c]
                              
    dydt[V.PSmad2_PSmad4_c] = x[C.kon_Smads]*y[V.PSmad2c]*y[V.Smad4c] - x[C.koff_Smads]*y[V.PSmad2_PSmad4_c] \
                              - x[C.kimp_Smads]*y[V.PSmad2_PSmad4_c]
                              
    dydt[V.PSmad2n] = Vcyt*x[C.kimp_Smad2]*y[V.PSmad2c]/Vnuc - x[C.kexp_Smad2]*y[V.PSmad2n] \
                      + x[C.koff_Smads]*y[V.PSmad2_Smad4_n] - x[C.kon_Smads]*y[V.PSmad2n]*y[V.Smad4n] \
                      - x[C.kdepho_Smad2]*y[V.PSmad2n] \
                      + 2*(x[C.koff_Smads]*y[V.PSmad2_PSmad2_n] - x[C.kon_Smads]*y[V.PSmad2n]*y[V.PSmad2n])

    dydt[V.PSmad2_PSmad2_n] = Vcyt *x[C.kimp_Smads]*y[V.PSmad2_PSmad2_c]/Vnuc - x[C.koff_Smads]*y[V.PSmad2_PSmad2_n] \
                              + x[C.kon_Smads]*y[V.PSmad2n]*y[V.PSmad2n]
                              
    dydt[V.PSmad2_Smad4_n] = Vcyt*x[C.kimp_Smads]*y[V.PSmad2_PSmad4_c]/Vnuc - x[C.koff_Smads]*y[V.PSmad2_Smad4_n] \
                             + x[C.kon_Smads]*y[V.PSmad2n]*y[V.Smad4n]
                             
    dydt[V.TGF_beta_endo] = x[C.kdiss_LRC]*y[V.LRC_endo] - x[C.kdeg_TGF_beta]*y[V.TGF_beta_endo]
    
    dydt[V.TGF_beta_ns] = x[C.kon_ns]*y[V.TGF_beta_ex] - koff_ns*y[V.TGF_beta_ns]
    
    return dydt