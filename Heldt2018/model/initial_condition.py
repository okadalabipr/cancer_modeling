from .name2idx import variables as V

def initial_values():
    y0=[0]*V.len_f_vars

    y0[V.tP21] = 0.6
    y0[V.aPcna] = 0.5
    y0[V.Rc] = 1
    y0[V.tCe] = 0.5
    y0[V.tCa] = 1.2
    y0[V.Pr] = 0.5

    return y0