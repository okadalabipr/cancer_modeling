from .name2idx import variables as V

def initial_values():
    y0 = [0]*V.len_f_vars

    y0[V.pro_IRcom] = 46.22225
    y0[V.IRcom] = 46.22225
    y0[V.p1IRcom] = 0
    y0[V.p2IRcom] = 0
    y0[V.p1p2IRcom] = 0
    y0[V.iAKT] = 4.33812
    y0[V.pAKT] = 0
    y0[V.imTOR] = 0.09592
    y0[V.pmTOR] = 0
    y0[V.iX] = 14.99133
    y0[V.pX] = 0
    y0[V.iS6K] = 2.77699
    y0[V.pS6K] = 0
    y0[V.iGSK3B] = 10.56415
    y0[V.pGSK3B] = 0
    y0[V.iFoxO1] = 0.43571
    y0[V.pFoxO1] = 0
    y0[V.G6Pase] = 38.54029

    return y0
