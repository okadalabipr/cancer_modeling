from .name2idx import parameters as C
from .name2idx import variables as V

def diffeq(y,t,*x):

    dydt = [0]*V.len_f_vars

    CycE = y[V.CycET] - y[V.CycEp27]
    CycA = y[V.CycAT] - y[V.CycAp27]

    Vdp27 = x[C.kd27] + (x[C.kd27e]*CycE + x[C.kd27a]*CycA)*y[V.Skp2]
    Vdcyce = x[C.kdcyce] + x[C.kdcycee]*CycE/(1.+x[C.Inhibitor]) + x[C.kdcycea]*CycA/(1.+x[C.Inhibitor])
    Vdcyca = x[C.kdcyca] + x[C.kdcycac1]*y[V.Cdh1]
    Vdskp2 = x[C.kdskp2] + x[C.kdskp2c1]*y[V.Cdh1]

    Vicdh1 = x[C.kicdh1e]*CycE/(1.+x[C.Inhibitor]) + x[C.kicdh1a]*CycA/(1.+x[C.Inhibitor])

    #protein
    dydt[V.p27T] = x[C.ks27] - Vdp27*y[V.p27T]
    dydt[V.Skp2] = x[C.ksskp2] - Vdskp2*y[V.Skp2]
    dydt[V.CycET] = x[C.kscyce] - Vdcyce*y[V.CycET]
    dydt[V.CycAT] = x[C.kscyca] - Vdcyca*y[V.CycAT]
    dydt[V.Emi1T] = x[C.ksemi1] - x[C.kdemi1]*y[V.Emi1T]

    dydt[V.CycEp27] = x[C.kasse]*(y[V.CycET]-y[V.CycEp27])*(y[V.p27T]-y[V.CycAp27]-y[V.CycEp27])-(x[C.kdise]+Vdp27+Vdcyce)*y[V.CycEp27]

    dydt[V.CycAp27] = x[C.kassa]*(y[V.CycAT]-y[V.CycAp27])*(y[V.p27T]-y[V.CycAp27]-y[V.CycEp27])-(x[C.kdisa]+Vdp27+Vdcyca)*y[V.CycAp27]

    dydt[V.EmiC] = x[C.kasec]*(x[C.Cdh1T]-y[V.EmiC])*(y[V.Emi1T]-y[V.EmiC]) - (x[C.kdiec]+x[C.kdemi1])*y[V.EmiC]

    dydt[V.Cdh1dp] = x[C.kacdh1]*(x[C.Cdh1T]-y[V.Cdh1dp]) - Vicdh1*y[V.Cdh1dp]

    dydt[V.Cdh1] = (x[C.kdiec]+x[C.kdemi1])*(y[V.Cdh1dp]-y[V.Cdh1]) - x[C.kasec]*y[V.Cdh1]*(y[V.Emi1T]-y[V.EmiC])+x[C.kacdh1]*(x[C.Cdh1T]-y[V.EmiC]-y[V.Cdh1])-Vicdh1*y[V.Cdh1]

    return dydt
