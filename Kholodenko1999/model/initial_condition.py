from .name2idx import variables as V

def initial_values():
    y0 = [0]*V.len_f_vars

    y0[V.EGF]=680
    y0[V.R]=100
    y0[V.PLCg]=105
    y0[V.Grb2]=85
    y0[V.SOS]=34
    y0[V.Shc]=150

    return y0