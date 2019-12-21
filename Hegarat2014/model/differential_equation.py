from .name2idx import parameters as C
from .name2idx import variables as V

def diffeq(y,t,*x):
    dydt = [0]*V.len_f_vars
    
    MPFa = y[V.MPF]/(1+x[C.RO])
    PP2a = y[V.PP2]/(1+x[C.OA])
    k25 = x[C.k25_d]*(x[C.Cdc25T] - y[V.Cdc25]) + x[C.k25_dd]* y[V.Cdc25]
    kwee = x[C.kwee_d]*(x[C.Wee1T] - y[V.Wee1]) + x[C.kwee_dd]*y[V.Wee1]
    

    dydt[V.MPF] = k25*(x[C.CycT] - y[V.MPF]) - kwee*y[V.MPF]
    dydt[V.Cdc25] = x[C.Va25]*MPFa*(x[C.Cdc25T] - y[V.Cdc25]) - x[C.Vi25]*PP2a*y[V.Cdc25]
    dydt[V.Wee1] = x[C.Vawee]*PP2a*(x[C.Wee1T] - y[V.Wee1]) - x[C.Viwee]*MPFa*y[V.Wee1]
    dydt[V.Gwl] = x[C.kagwl]*MPFa*(x[C.GwlT]-y[V.Gwl]) \
                  - (x[C.kigwl_d]+x[C.kigwl_dd]*x[C.PP2T]/(1+x[C.OA]) + x[C.kigwl]*PP2a)*y[V.Gwl]
    dydt[V.ENSAPt] = x[C.kaensa]*y[V.Gwl]*(x[C.ENSAT] - y[V.ENSAPt]) - x[C.kiensa]*y[V.ENSAPt]
    dydt[V.PP2] = -x[C.kas]*(y[V.ENSAPt] - (x[C.PP2T] - y[V.PP2]))*y[V.PP2] \
                   + (x[C.kdis] + x[C.kiensa]) *(x[C.PP2T] - y[V.PP2])
    
    return dydt