from .name2idx import parameters as C

def f_params():
    x = [0]*C.len_f_params

    x[C.TR] = 0
    x[C.a1] = 0.5
    x[C.a2] = 0.2
    x[C.t1] = 0.1
    x[C.a3] = 1
    x[C.t2] = 0.1
    x[C.c1a] = 5e-7
    x[C.c2a] = 0
    x[C.c3a] = 4e-4
    x[C.c4a] = 0.5
    x[C.c5a] = 1e-4
    x[C.c6a] = 2e-5
    x[C.c1] = 5e-7
    x[C.c2] = 0
    x[C.c3] = 4e-4
    x[C.c4] = 0.5
    x[C.c5] = 3e-4
    x[C.k1] = 2.5e-3
    x[C.k2] = 0.1
    x[C.k3] = 1.5e-3
    x[C.kprod] = 2.5e-5
    x[C.kdeg] = 1.25e-4
    x[C.kv] = 5
    x[C.i1] = 2.5e-3
    x[C.e2a] = 1e-2
    x[C.i1a] = 1e-3
    x[C.e1a] = 5e-4
    x[C.c1c] = 5e-7
    x[C.c2c] = 0
    x[C.c3c] = 4e-4

    return x