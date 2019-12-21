from .name2idx import parameters as C

def f_params():
    x = [0]*C.len_f_params

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