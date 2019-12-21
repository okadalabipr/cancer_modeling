from .name2idx import variables as V

def initial_values():
    y0 = [0]*V.len_f_vars

    y0[V.MB] = 9.0
    y0[V.BC] = 2.0
    y0[V.BN] = 1.9
    y0[V.MC] = 1.4
    y0[V.MP] = 1.6
    y0[V.PCN] = 1.0

    return y0