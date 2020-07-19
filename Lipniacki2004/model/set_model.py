from .name2idx import C, V

def diffeq(y, t, *x):
    dydt = [0] * V.NUM

    dydt[V.IKKn]=x[C.kprod]-x[C.kdeg]*y[V.IKKn]-x[C.TR]*x[C.k1]*y[V.IKKn]                                                               # neutral IKK   
    dydt[V.IKKa]=x[C.TR]*x[C.k1]*y[V.IKKn]-x[C.k3]*y[V.IKKa]-x[C.TR]*x[C.k2]*y[V.IKKa]*y[V.A20]\
                -x[C.kdeg]*y[V.IKKa]-x[C.a2]*y[V.IKKa]*y[V.IkBa]+x[C.t1]*y[V.IKKIkBa]\
                -x[C.a3]*y[V.IKKa]*y[V.IkBaNFkB]+x[C.t2]*y[V.IKKIkBaNFkB]                                                               # free active IKK                                                                                    
    dydt[V.IKKi]=x[C.k3]*y[V.IKKa]+x[C.TR]*x[C.k2]*y[V.IKKa]*y[V.A20]-x[C.kdeg]*y[V.IKKi]                                               # inactive IKK   
    dydt[V.IKKIkBa]=x[C.a2]*y[V.IKKa]*y[V.IkBa]-x[C.t1]*y[V.IKKIkBa]                                                                    # cytoplasmic (IKK|IkBa) complex 
    dydt[V.IKKIkBaNFkB]=x[C.a3]*y[V.IKKa]*y[V.IkBaNFkB]-x[C.t2]*y[V.IKKIkBaNFkB]                                                        # cytoplasmic (IKK|IkBa|NFkB) complex
    dydt[V.NFkB]=x[C.c6a]*y[V.IkBaNFkB]-x[C.a1]*y[V.NFkB]*y[V.IkBa]+x[C.t2]*y[V.IKKIkBaNFkB]-x[C.i1]*y[V.NFkB]                          # free cytoplasmic NFkB
    dydt[V.NFkBn]=x[C.i1]*x[C.kv]*y[V.NFkB]-x[C.a1]*y[V.IkBan]*y[V.NFkBn]                                                               # free nuclear NFkB
    dydt[V.A20]=x[C.c4]*y[V.A20t]-x[C.c5]*y[V.A20]                                                                                      # cytoplasmic A20
    dydt[V.A20t]=x[C.c2]+x[C.c1]*y[V.NFkBn]-x[C.c3]*y[V.A20t]                                                                           # A20 transcription
    dydt[V.IkBa]=-x[C.a2]*y[V.IKKa]*y[V.IkBa]-x[C.a1]*y[V.IkBa]*y[V.NFkB]\
                +x[C.c4a]*y[V.IkBat]-x[C.c5a]*y[V.IkBa]-x[C.i1a]*y[V.IkBa]+x[C.e1a]*y[V.IkBan]                                          # free cytoplasmic IkBa
    dydt[V.IkBan]=-x[C.a1]*y[V.IkBan]*y[V.NFkBn]+x[C.i1a]*x[C.kv]*y[V.IkBa]-x[C.e1a]*x[C.kv]*y[V.IkBan]                                 # free nuclear IkBan
    dydt[V.IkBat]=x[C.c2a]+x[C.c1a]*y[V.NFkBn]-x[C.c3a]*y[V.IkBat]                                                                      # IkB transcription
    dydt[V.IkBaNFkB]=x[C.a1]*y[V.IkBa]*y[V.NFkB]-x[C.c6a]*y[V.IkBaNFkB]-x[C.a3]*y[V.IKKa]*y[V.IkBaNFkB]+x[C.e2a]*y[V.IkBanNFkBn]        # cytoplasmic (IkBa|NFkB) complex
    dydt[V.IkBanNFkBn]=x[C.a1]*y[V.IkBan]*y[V.NFkBn]-x[C.e2a]*x[C.kv]*y[V.IkBanNFkBn]                                                   # Nuclear (IkBa|NFkB) complex
    dydt[V.cgent]=x[C.c2c]+x[C.c1c]*y[V.NFkBn]-x[C.c3c]*y[V.cgent]                                                                      # cgen mRNA
    
    return dydt


def param_values():
    x = [0] * C.NUM

    x[C.TR] = 0
    x[C.a1] = 0.5
    x[C.a2] = 0.2
    x[C.t1] = 0.1
    x[C.a3] = 1
    x[C.t2] = 0.1
    x[C.c1a] = 5e-7
    x[C.c2a] = 0
    x[C.c3a] = 4e-4
    x[C.c4a] = 0.5
    x[C.c5a] = 1e-4
    x[C.c6a] = 2e-5
    x[C.c1] = 5e-7
    x[C.c2] = 0
    x[C.c3] = 4e-4
    x[C.c4] = 0.5
    x[C.c5] = 3e-4
    x[C.k1] = 2.5e-3
    x[C.k2] = 0.1
    x[C.k3] = 1.5e-3
    x[C.kprod] = 2.5e-5
    x[C.kdeg] = 1.25e-4
    x[C.kv] = 5
    x[C.i1] = 2.5e-3
    x[C.e2a] = 1e-2
    x[C.i1a] = 1e-3
    x[C.e1a] = 5e-4
    x[C.c1c] = 5e-7
    x[C.c2c] = 0
    x[C.c3c] = 4e-4

    return x


def initial_values():
    y0 = [0] * V.NUM
    
    y0[V.IkBaNFkB] = 0.06

    return y0