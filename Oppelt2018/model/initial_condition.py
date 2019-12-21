from .name2idx import variables as V

def initial_values():
    y0 = [0]*V.len_f_vars

    y0[V.TNFR]     = 0.
    y0[V.Ikk]      = 1.
    y0[V.pIkk]     = 0.
    y0[V.ppIkk]    = 0.
    y0[V.iIkk]     = 0.
    y0[V.NfkIkb]   = 1.
    y0[V.NfkpIkb]  = 0.
    y0[V.pNfkIkb]  = 0.
    y0[V.pNfk]     = 0.
    y0[V.Nfk]      = 0.
    y0[V.pIkb]     = 0.
    y0[V.Ikb]      = 0.
    y0[V.mIkb]     = 0.
    y0[V.nIkb]     = 0.
    y0[V.pnNfk]    = 0.
    y0[V.nNfk]     = 0.
    y0[V.nNfkIkb]  = 0.
    y0[V.RnaA20_1] = 0.
    y0[V.RnaA20]   = 0.
    y0[V.A20]      = 0.

    return y0