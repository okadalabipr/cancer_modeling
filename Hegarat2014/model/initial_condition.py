from .name2idx import variables as V

def initial_values():
    y0 = [0]*V.len_f_vars
    
    y0[V.MPF] = 0
    y0[V.Cdc25] = 0 
    y0[V.Wee1] = 1
    y0[V.Gwl] = 0
    y0[V.ENSAPt] = 0
    y0[V.PP2] = 0.5

    return y0