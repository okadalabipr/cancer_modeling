from .name2idx import C, V


def diffeq(y, t, *x):
    dydt = [0]*V.NUM

    dydt[V.MAP2K] = x[C.k0]*y[V.S]*(1-y[V.MAP2K]) - x[C.k1]*y[V.MAP2K]
    dydt[V.MAPK] = x[C.k2]*y[V.MAP2K]*(1-y[V.MAPK]) - x[C.k3]*y[V.MKP1]*y[V.MAPK]/(x[C.k4]+y[V.MAPK])
    dydt[V.MKP1RNA] = x[C.k5]*y[V.MAPK]*(1-y[V.MKP1RNA])-x[C.k6]*y[V.MKP1RNA]
    dydt[V.MKP1] = x[C.k7]*y[V.MKP1RNA]*(1-y[V.MKP1]) - x[C.k8]*y[V.MKP1]
    dydt[V.FRET] = x[C.k9]*y[V.MAPK]*(1-y[V.FRET])-x[C.k10]*y[V.FRET]

    return dydt


def param_values():
    x = [0] * C.NUM

    x[C.k0] = 0.06
    x[C.k1] = 0.15
    x[C.k2] = 0.15
    x[C.k3] = 0.16
    x[C.k4] = 0.0001
    x[C.k5] = 0.055
    x[C.k6] = 0.05
    x[C.k7] = 0.20
    x[C.k8] = 0.02
    x[C.k9] = 0.2
    x[C.k10] = 0.05
    x[C.k11] = 0.05
    x[C.k12] = 0.001

    return x


def initial_values():
    y0 = [0] * V.NUM

    y0[V.S] = 1

    return y0