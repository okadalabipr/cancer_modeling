from .name2idx import variables as V

def initial_values():
    y0 = [0]*V.len_f_vars
    
    y0[V.Rec] = 1.3
    y0[V.Rec_i] = 113.194
    y0[V.JAK2] = 2.8
    y0[V.SHP1] = 91.0
    y0[V.STAT5] = 165.0
    y0[V.DecoyR] = 3.4

    return y0