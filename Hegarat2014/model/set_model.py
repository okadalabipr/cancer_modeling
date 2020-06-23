from .name2idx import C, V

def diffeq(y,t,*x):

    dydt = [0] * V.NUM
    
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


def param_values():

    x = [0] * C.NUM

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


def initial_values():

    y0 = [0] * V.NUM
    
    y0[V.MPF] = 0
    y0[V.Cdc25] = 0 
    y0[V.Wee1] = 1
    y0[V.Gwl] = 0
    y0[V.ENSAPt] = 0
    y0[V.PP2] = 0.5

    return y0