# Table S6: List of differential equations of the reduced model
from .name2idx import parameters as C
from .name2idx import variables as V

def diffeq(y,t,*x):
    dydt = [0]*V.len_f_vars

    dydt[V.TNFR]     = 1*x[C.uptake]*x[C.TNF] -1*x[C.deact_TNFR]*y[V.TNFR]
    dydt[V.Ikk]      = -1*(x[C.act_Ikk_by_TNF]*y[V.TNFR]*y[V.Ikk]) +1*(x[C.trigger_iIkk]*y[V.iIkk])
    dydt[V.pIkk]     = 1*(x[C.act_Ikk_by_TNF]*y[V.TNFR]*y[V.Ikk]) -1*(x[C.act_pIkk]*y[V.pIkk])
    dydt[V.ppIkk]    = 1*(x[C.act_pIkk]*y[V.pIkk]) -1*(x[C.deact_ppIkk]*y[V.ppIkk])
    dydt[V.iIkk]     = 1*(x[C.deact_ppIkk]*y[V.ppIkk]) -1*(x[C.trigger_iIkk]*y[V.iIkk])
    dydt[V.NfkIkb]   = -1*((x[C.act_Ikb_by_Ikk])*y[V.pIkk]*y[V.NfkIkb]) -1*((x[C.act_Nfk_by_Ikk])*y[V.pIkk]*
                       y[V.NfkIkb]) +1*(x[C.form_complex]*y[V.Nfk]*y[V.Ikb]) +1*(x[C.ext_nNfkIkb]*y[V.nNfkIkb])\
                       *(x[C.Vnuc]/1)
    dydt[V.NfkpIkb]  = 1*((x[C.act_Ikb_by_Ikk])*y[V.pIkk]*y[V.NfkIkb]) -1*((x[C.act_Nfk_by_Ikk_complex])*
                       y[V.pIkk]*y[V.NfkpIkb]) -1*(x[C.split_NfkpIkb]*y[V.NfkpIkb])
    dydt[V.pNfkIkb]  = -1*((x[C.act_Ikb_complex])*y[V.pNfkIkb]) -1*((x[C.act_Ikb_by_Ikk])*y[V.pIkk]*
                       y[V.pNfkIkb]) +1*((x[C.act_Nfk_by_Ikk])*y[V.pIkk]*y[V.NfkIkb])
    dydt[V.pNfkpIkb] = 1*((x[C.act_Ikb_complex])*y[V.pNfkIkb]) +1*((x[C.act_Ikb_by_Ikk])*y[V.pIkk]*
                       y[V.pNfkIkb]) +1*((x[C.act_Nfk_by_Ikk_complex])*y[V.pIkk]*y[V.NfkpIkb]) -1*\
                       (x[C.split_NfkIkb]*y[V.pNfkpIkb])
    dydt[V.pNfk]     = 1*(x[C.split_NfkIkb]*y[V.pNfkpIkb]) -1*((x[C.int_Nfk]*x[C.eta_int_pNfk])*y[V.pNfk])
    dydt[V.Nfk]      = 1*(x[C.split_NfkpIkb]*y[V.NfkpIkb]) -1*(x[C.form_complex]*y[V.Nfk]*y[V.Ikb]) -1*\
                       ((x[C.int_Nfk])*y[V.Nfk])
    dydt[V.pIkb]     = 1*(x[C.split_NfkpIkb]*y[V.NfkpIkb]) +1*(x[C.split_NfkIkb]*y[V.pNfkpIkb]) -1*\
                       (x[C.degrad_Ikb]*y[V.pIkb])
    dydt[V.Ikb]      = -1*(x[C.form_complex]*y[V.Nfk]*y[V.Ikb]) +1*(x[C.prod_Ikb]*y[V.mIkb]) -1*(x[C.int_Ikb]*
                       y[V.Ikb])
    dydt[V.mIkb]     = 1*(x[C.prod_mIkb_by_nNfk]*y[V.nNfk]) -1*(x[C.degrad_mIkb]*y[V.mIkb])
    dydt[V.nIkb]     = 1*(x[C.int_Ikb]*y[V.Ikb])*(1/x[C.Vnuc]) -1*(x[C.form_complex_nuc]*y[V.nNfk]*y[V.nIkb])
    dydt[V.pnNfk]    = 1*((x[C.int_Nfk]*x[C.eta_int_pNfk])*y[V.pNfk])*(1/x[C.Vnuc]) -1*(x[C.deact_pnNfk]*
                       y[V.pnNfk])
    dydt[V.nNfk]     = 1*((x[C.int_Nfk])*y[V.Nfk])*(1/x[C.Vnuc]) +1*(x[C.deact_pnNfk]*y[V.pnNfk]) -1*\
                       (x[C.form_complex_nuc]*y[V.nNfk]*y[V.nIkb])
    dydt[V.nNfkIkb]  = 1*(x[C.form_complex_nuc]*y[V.nNfk]*y[V.nIkb]) -1*(x[C.ext_nNfkIkb]*y[V.nNfkIkb])
    dydt[V.RnaA20_1] = 1*(x[C.build_RnaA20]*y[V.nNfk]) -1*(x[C.shuttle_RnaA20]*y[V.RnaA20_1])
    dydt[V.RnaA20]   = 1*(x[C.shuttle_RnaA20]*y[V.RnaA20_1]) -1*(x[C.degrad_RnaA20]*y[V.RnaA20])
    dydt[V.A20]      = 1*(x[C.build_A20]*y[V.RnaA20]) -1*(x[C.degrad_A20]*y[V.A20])

    return dydt