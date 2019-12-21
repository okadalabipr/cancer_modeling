from .name2idx import variables as V

def initial_values():
    y0 = [0]*V.len_f_vars
    
    y0[V.IkBaNFkB] = 0.06

    return y0