# Table S9: List of model parameters (part 2) as being employed for numeric integration of the model ODEs.
from .name2idx import parameters as C

def f_params():
    x = [0]*C.len_f_params

    x[C.k1_synthesis] = 0.04780
    x[C.k1_InsIRcom] = 7.78161
    x[C.k2_InsIRcom] = 1.61148
    x[C.k1_p1IRcomDeg] = 0.00792
    x[C.k1_p1IRcomPhos] = 0.00004
    x[C.k1_p1p2IRcomdePhos] = 0.28443
    x[C.k1_IRcomPhos] = 9.93311
    x[C.k1_p2IRcomdePhos] = 0.00001
    x[C.k1_p2IRcomDeg] = 0.00001
    x[C.k1_Insp2IRcom] = 0.36303
    x[C.k2_Insp2IRcom] = 0.40813
    x[C.k1_p1p2IRcomDeg] = 0.09490
    x[C.k1_AKTPhos] = 0.00920
    x[C.k1_pAKTdePhos] = 7.70619
    x[C.k1_mTORPhos] = 0.41968
    x[C.k1_pmTORdePhos] = 0.12433
    x[C.k1_S6KPhos] = 0.00752
    x[C.k1_pS6KdePhos] = 1.95498
    x[C.k1_XPhos] = 0.00105
    x[C.k1_pXdePhos] = 0.00146
    x[C.k1_GSK3BPhos] = 2.97538
    x[C.k1_pGSK3BdePhos] = 0.92460
    x[C.k1_FoxO1Phos] = 4.59698
    x[C.k1_pFoxO1dePhos] = 0.15172
    x[C.k1_G6PaseSynthesis] = 4.86146
    x[C.k1_G6PaseDeg] = 0.05496

    return x
