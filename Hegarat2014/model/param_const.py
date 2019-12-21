from .name2idx import parameters as C

def f_params():
    x = [0]*C.len_f_params

    x[C.CycT] = 1
    x[C.Va25] = 2
    x[C.Vi25] = 2
    x[C.Vawee] = 2 
    x[C.Viwee] = 2
    x[C.kagwl] = 10
    x[C.kigwl] = 2
    x[C.kigwl_d] = 0.02
    x[C.kigwl_dd] = 0
    x[C.kaensa] = 2
    x[C.kiensa] = 0.6
    x[C.kas] = 100
    x[C.kdis] = 1
    x[C.Cdc25T] = 1
    x[C.Wee1T] = 1
    x[C.GwlT] = 1
    x[C.ENSAT] = 1
    x[C.PP2T] = 0.5
    x[C.k25_d] = 0.01
    x[C.k25_dd] = 1
    x[C.kwee_d] = 0.01
    x[C.kwee_dd] = 1
    x[C.RO] = 0
    x[C.OA] = 0

    return x