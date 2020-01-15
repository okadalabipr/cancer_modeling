# Table S6: List of differential equations of the reduced model
from .name2idx import parameters as C
from .name2idx import variables as V


def insulin(y, t):
    if t < 2400:
        """steady state
        """
        return 0.01
    else:
        return y[V.Ins]


def diffeq(y,t,*x):
    re = [0]*25
    re[1] = x[C.k1_synthesis] * (y[V.pro_IRcom] - y[V.IRcom])
    re[2] = x[C.k1_InsIRcom] * insulin(y, t) * y[V.IRcom] - x[C.k2_InsIRcom] * y[V.p1IRcom]
    re[3] = x[C.k1_p1IRcomDeg] * y[V.p1IRcom]
    re[4] = x[C.k1_p1IRcomPhos] * y[V.pmTOR] * y[V.p1IRcom]
    re[5] = x[C.k1_p1p2IRcomdePhos] * y[V.p1p2IRcom]
    re[6] = x[C.k1_IRcomPhos] * y[V.pmTOR] * y[V.IRcom]
    re[7] = x[C.k1_p2IRcomdePhos] * y[V.p2IRcom]
    re[8] = x[C.k1_p2IRcomDeg] * y[V.p2IRcom]
    re[9] = x[C.k1_Insp2IRcom] * insulin(y, t) * y[V.p2IRcom] - x[C.k2_Insp2IRcom] * y[V.p1p2IRcom]
    re[10] = x[C.k1_p1p2IRcomDeg] * y[V.p1p2IRcom]
    re[11] = x[C.k1_AKTPhos] * (y[V.iAKT] - y[V.pAKT]) * y[V.p1IRcom]
    re[12] = x[C.k1_pAKTdePhos] * y[V.pAKT]
    re[13] = x[C.k1_mTORPhos] * (y[V.imTOR] - y[V.pmTOR]) * y[V.pAKT]
    re[14] = x[C.k1_pmTORdePhos] * y[V.pmTOR]
    re[15] = x[C.k1_S6KPhos] * (y[V.iS6K] - y[V.pS6K]) * y[V.pmTOR]
    re[16] = x[C.k1_pS6KdePhos] * y[V.pS6K] * y[V.pX]
    re[17] = x[C.k1_XPhos] * (y[V.iX] - y[V.pX]) * y[V.pmTOR]
    re[18] = x[C.k1_pXdePhos] * y[V.pX]
    re[19] = x[C.k1_GSK3BPhos] * (y[V.iGSK3B] - y[V.pGSK3B]) * y[V.pAKT]
    re[20] = x[C.k1_pGSK3BdePhos] * y[V.pGSK3B]
    re[21] = x[C.k1_FoxO1Phos] * (y[V.iFoxO1] - y[V.pFoxO1]) * y[V.pAKT]
    re[22] = x[C.k1_pFoxO1dePhos] * y[V.pFoxO1]
    re[23] = x[C.k1_G6PaseSynthesis] * (y[V.iFoxO1] - y[V.pFoxO1])
    re[24] = x[C.k1_G6PaseDeg] * y[V.G6Pase]
    
    dydt = [0]*V.len_f_vars
    
    dydt[V.IRcom] = re[1] - re[2] - re[6] + re[7]
    dydt[V.p1IRcom] = re[2] - re[3] -re[4] + re[5]
    dydt[V.p2IRcom] = re[6] - re[7] - re[8] - re[9]
    dydt[V.p1p2IRcom] = re[4] - re[5] + re[9] - re[10]
    dydt[V.pAKT] = re[11] - re[12]
    dydt[V.pmTOR] = re[13] - re[14]
    dydt[V.pX] = re[17] - re[18]
    dydt[V.pS6K] = re[15] - re[16]
    dydt[V.pGSK3B] = re[19] - re[20]
    dydt[V.pFoxO1] = re[21] - re[22]
    dydt[V.G6Pase] = re[23] - re[24]

    return dydt
