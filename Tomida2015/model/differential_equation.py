from .name2idx import parameters as C
from .name2idx import variables as V

def diffeq(y,t,*x):
    dydt = [0]*V.len_f_vars

    dydt[V.MAP2K] = x[C.k0]*y[V.S]*(1-y[V.MAP2K]) - x[C.k1]*y[V.MAP2K]
    dydt[V.MAPK] = x[C.k2]*y[V.MAP2K]*(1-y[V.MAPK]) - x[C.k3]*y[V.MKP1]*y[V.MAPK]/(x[C.k4]+y[V.MAPK])
    dydt[V.MKP1RNA] = x[C.k5]*y[V.MAPK]*(1-y[V.MKP1RNA])-x[C.k6]*y[V.MKP1RNA]
    dydt[V.MKP1] = x[C.k7]*y[V.MKP1RNA]*(1-y[V.MKP1]) - x[C.k8]*y[V.MKP1]
    dydt[V.FRET] = x[C.k9]*y[V.MAPK]*(1-y[V.FRET])-x[C.k10]*y[V.FRET]

    return dydt