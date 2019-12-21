from .name2idx import parameters as C
from .name2idx import variables as V

def diffeq(y,t,*x):
    dydt = [0]*V.len_f_vars

    dydt[V.IKKn]=x[C.kprod]-x[C.kdeg]*y[V.IKKn]-x[C.TR]*x[C.k1]*y[V.IKKn]                                                               # neutral IKK   
    dydt[V.IKKa]=x[C.TR]*x[C.k1]*y[V.IKKn]-x[C.k3]*y[V.IKKa]-x[C.TR]*x[C.k2]*y[V.IKKa]*y[V.A20]-\
        x[C.kdeg]*y[V.IKKa]-x[C.a2]*y[V.IKKa]*y[V.IkBa]+x[C.t1]*y[V.IKKIkBa]-x[C.a3]*y[V.IKKa]*y[V.IkBaNFkB]+x[C.t2]*y[V.IKKIkBaNFkB]   # free active IKK                                                                                    
    dydt[V.IKKi]=x[C.k3]*y[V.IKKa]+x[C.TR]*x[C.k2]*y[V.IKKa]*y[V.A20]-x[C.kdeg]*y[V.IKKi]                                               # inactive IKK   
    dydt[V.IKKIkBa]=x[C.a2]*y[V.IKKa]*y[V.IkBa]-x[C.t1]*y[V.IKKIkBa]                                                                    # cytoplasmic (IKK|IkBa) complex 
    dydt[V.IKKIkBaNFkB]=x[C.a3]*y[V.IKKa]*y[V.IkBaNFkB]-x[C.t2]*y[V.IKKIkBaNFkB]                                                        # cytoplasmic (IKK|IkBa|NFkB) complex
    dydt[V.NFkB]=x[C.c6a]*y[V.IkBaNFkB]-x[C.a1]*y[V.NFkB]*y[V.IkBa]+x[C.t2]*y[V.IKKIkBaNFkB]-x[C.i1]*y[V.NFkB]                          # free cytoplasmic NFkB
    dydt[V.NFkBn]=x[C.i1]*x[C.kv]*y[V.NFkB]-x[C.a1]*y[V.IkBan]*y[V.NFkBn]                                                               # free nuclear NFkB
    dydt[V.A20]=x[C.c4]*y[V.A20t]-x[C.c5]*y[V.A20]                                                                                      # cytoplasmic A20
    dydt[V.A20t]=x[C.c2]+x[C.c1]*y[V.NFkBn]-x[C.c3]*y[V.A20t]                                                                           # A20 transcription
    dydt[V.IkBa]=-x[C.a2]*y[V.IKKa]*y[V.IkBa]-x[C.a1]*y[V.IkBa]*y[V.NFkB]+x[C.c4a]*y[V.IkBat]-\
        x[C.c5a]*y[V.IkBa]-x[C.i1a]*y[V.IkBa]+x[C.e1a]*y[V.IkBan]                                                                       # free cytoplasmic IkBa
    dydt[V.IkBan]=-x[C.a1]*y[V.IkBan]*y[V.NFkBn]+x[C.i1a]*x[C.kv]*y[V.IkBa]-x[C.e1a]*x[C.kv]*y[V.IkBan]                                 # free nuclear IkBan
    dydt[V.IkBat]=x[C.c2a]+x[C.c1a]*y[V.NFkBn]-x[C.c3a]*y[V.IkBat]                                                                      # IkB transcription
    dydt[V.IkBaNFkB]=x[C.a1]*y[V.IkBa]*y[V.NFkB]-x[C.c6a]*y[V.IkBaNFkB]-x[C.a3]*y[V.IKKa]*y[V.IkBaNFkB]+x[C.e2a]*y[V.IkBanNFkBn]        # cytoplasmic (IkBa|NFkB) complex
    dydt[V.IkBanNFkBn]=x[C.a1]*y[V.IkBan]*y[V.NFkBn]-x[C.e2a]*x[C.kv]*y[V.IkBanNFkBn]                                                   # Nuclear (IkBa|NFkB) complex
    dydt[V.cgent]=x[C.c2c]+x[C.c1c]*y[V.NFkBn]-x[C.c3c]*y[V.cgent]                                                                      # cgen mRNA
    
    return dydt