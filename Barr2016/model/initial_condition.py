from .name2idx import variables as V

def initial_values():
    y0 = [0]*V.len_f_vars

    y0[V.Cdh1dp] = 1.
    y0[V.Cdh1] = 1.

    return y0