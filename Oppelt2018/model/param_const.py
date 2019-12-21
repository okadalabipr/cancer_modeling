# Table S9: List of model parameters (part 2) as being employed for numeric integration of the model ODEs.
from .name2idx import parameters as C

def f_params_noDCF():
    x = [0]*C.len_f_params

    x[C.uptake] = 1.0000
    x[C.TNF] = 1.0000
    x[C.trigger_iIkk] = 0.0041
    x[C.deact_TNFR] = 0.0010
    x[C.deact_ppIkk] = 0.1660
    x[C.deact_pnNfk] = 1000.0000
    x[C.act_Ikk_by_TNF] = 0.0714
    x[C.act_pIkk] = 0.0648
    x[C.act_Ikb_by_Ikk] = 0.3980
    x[C.act_Nfk_by_Ikk] = 0.6438
    x[C.act_Nfk_by_Ikk_complex] = 0.2816
    x[C.act_Ikb_complex] = 1.3897
    x[C.form_complex] = 2.8390
    x[C.form_complex_nuc] = 1000.0000
    x[C.ext_nNfkIkb] = 1000.0000
    x[C.Vnuc] = 1.0000
    x[C.split_NfkpIkb] = 0.0811
    x[C.split_NfkIkb] = 1.0000
    x[C.int_Nfk] = 0.0100
    x[C.int_Ikb] = 0.1226
    x[C.eta_int_pNfk] = 17.9585
    x[C.degrad_Ikb] = 0.6308
    x[C.degrad_mIkb] = 0.0313
    x[C.degrad_RnaA20] = 0.0089
    x[C.degrad_A20] = 0.0116
    x[C.prod_Ikb] = 1.0000
    x[C.prod_mIkb_by_nNfk] = 0.0047
    x[C.build_RnaA20] = 1.0000
    x[C.build_A20] = 0.0006
    x[C.shuttle_RnaA20] = 0.0311

    return x

def f_params_DCF():
    x = [0]*C.len_f_params

    x[C.uptake] = 1.0000
    x[C.TNF] = 1.0000
    x[C.trigger_iIkk] = 0.0195
    x[C.deact_TNFR] = 0.0010
    x[C.deact_ppIkk] = 0.1660
    x[C.deact_pnNfk] = 1000.0000
    x[C.act_Ikk_by_TNF] = 0.0347
    x[C.act_pIkk] = 0.1603
    x[C.act_Ikb_by_Ikk] = 0.1562
    x[C.act_Nfk_by_Ikk] = 0.6438
    x[C.act_Nfk_by_Ikk_complex] = 0.2816
    x[C.act_Ikb_complex] = 1.3897
    x[C.form_complex] = 2.8390
    x[C.form_complex_nuc] = 1000.0000
    x[C.ext_nNfkIkb] = 1000.0000
    x[C.Vnuc] = 1.0000
    x[C.split_NfkpIkb] = 0.0811
    x[C.split_NfkIkb] = 1.0000
    x[C.int_Nfk] = 0.0100
    x[C.int_Ikb] = 0.1226
    x[C.eta_int_pNfk] = 17.9585
    x[C.degrad_Ikb] = 0.6308
    x[C.degrad_mIkb] = 0.0053
    x[C.degrad_RnaA20] = 0.0089
    x[C.degrad_A20] = 0.0116
    x[C.prod_Ikb] = 1.0000
    x[C.prod_mIkb_by_nNfk] = 0.0020
    x[C.build_RnaA20] = 1.0000
    x[C.build_A20] = 0.0006
    x[C.shuttle_RnaA20] = 0.0119

    return x