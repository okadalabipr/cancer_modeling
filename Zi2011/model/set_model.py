import numpy as np

from .name2idx import C, V

def diffeq(y, t, *x):
    dydt = [0] * V.NUM
    
            
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


def param_values():
    x = [0] * C.NUM

    x[C.kdeg_T1R] = 0.00256
    x[C.kdeg_T2R] = 0.0132
    x[C.kdeg_LRC] = 0.00256
    x[C.kdeg_TGF_beta] = 0.347
    x[C.kprod_T1R] = 0.0137
    x[C.ki] = 0.333
    x[C.kr] = 0.0333
    x[C.kimp_Smad2] = 0.156
    x[C.kexp_Smad2] = 0.739
    x[C.kimp_Smad4] = 0.156
    x[C.kexp_Smad4] = 0.355
    x[C.kimp_Smads] = 0.889
    x[C.koff_Smads] = 1
    x[C.kdepho_Smad2] = 0.394
    
    x[C.kprod_T2R] = 0.0190076
    x[C.ka_LRC] = 117.897
    x[C.kdiss_LRC] = 0.0438111
    x[C.klid] = 0.0233678
    x[C.kpho_Smad2] = 0.0488268
    x[C.kon_Smads] = 0.198472
    x[C.kon_ns] = 0.0505413
    x[C.KD_ns] = 40.2257

    return x


def initial_values():
    y0 = [0] * V.NUM

    y0[V.TGF_beta_ex] = 0.001*50
    y0[V.T1R_surf] = 0.702494
    y0[V.T1R_endo] = 6.52344
    y0[V.T2R_surf] = 0.201077
    y0[V.T2R_endo] = 1.43997
    y0[V.LRC_surf] = 0
    y0[V.LRC_endo] = 0
    y0[V.Smad2c] = 60.6
    y0[V.Smad2n] = 28.5
    y0[V.Smad4c] = 50.8
    y0[V.Smad4n] = 50.8
    y0[V.PSmad2c] = 0
    y0[V.PSmad2_PSmad2_c] = 0
    y0[V.PSmad2_PSmad4_c] = 0
    y0[V.PSmad2n] = 0
    y0[V.PSmad2_PSmad2_n] = 0
    y0[V.PSmad2_Smad4_n] = 0
    y0[V.TGF_beta_endo] = 0
    y0[V.TGF_beta_ns] = 0

    return y0
