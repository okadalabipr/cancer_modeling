from .name2idx import variables as V

def initial_values():
    y0 = [0]*V.len_f_vars

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
