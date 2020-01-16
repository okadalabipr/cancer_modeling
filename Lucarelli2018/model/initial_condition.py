from .name2idx import variables as V

from model.name2idx import parameters as C
from model.param_const import f_params

def initial_values():
    y0 = [0]*V.len_f_vars

    x = f_params()

    y0[V.TGFb] = 1
    y0[V.Rec] = 1.84
    y0[V.TGFb_pRec] = 0
    y0[V.S2] = 1.43e2
    y0[V.S3] = 1.63e1
    y0[V.S4] = 6.71e1
    y0[V.ppS2_ppS2_ppS2] = 0
    y0[V.ppS3_ppS3_ppS3] = 0
    y0[V.S4_S4_S4] = 0
    y0[V.pS2] = 0
    y0[V.pS3] = 0
    y0[V.ppS2] = 0
    y0[V.ppS3] = 0
    y0[V.ppS2_ppS2_S4] = 0
    y0[V.ppS2_ppS2_ppS3] = 0
    y0[V.ppS2_ppS3_ppS3] = 0
    y0[V.ppS3_ppS3_S4] = 0
    y0[V.ppS2_ppS3_S4] = 0
    y0[V.ppS3_S4_S4] = 0
    y0[V.ppS2_S4_S4] = 0
    y0[V.gene] = 1
    return y0