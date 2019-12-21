from .name2idx import parameters as C

def f_params():
    x = [0]*C.len_f_params

    x[C.k0] = 0.06
    x[C.k1] = 0.15
    x[C.k2] = 0.15
    x[C.k3] = 0.16
    x[C.k4] = 0.0001
    x[C.k5] = 0.055
    x[C.k6] = 0.05
    x[C.k7] = 0.20
    x[C.k8] = 0.02
    x[C.k9] = 0.2
    x[C.k10] = 0.05
    x[C.k11] = 0.05
    x[C.k12] = 0.001

    return x