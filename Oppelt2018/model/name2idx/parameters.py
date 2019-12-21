param_names = [\
    'uptake',
    'TNF',
    'trigger_iIkk',
    'deact_TNFR',
    'deact_ppIkk',
    'deact_pnNfk',
    'act_Ikk_by_TNF',
    'act_pIkk',
    'act_Ikb_by_Ikk',
    'act_Nfk_by_Ikk',
    'act_Nfk_by_Ikk_complex',
    'act_Ikb_complex',
    'form_complex',
    'form_complex_nuc',
    'ext_nNfkIkb',
    'Vnuc',
    'split_NfkpIkb',
    'split_NfkIkb',
    'int_Nfk',
    'int_Ikb',
    'eta_int_pNfk',
    'degrad_Ikb',
    'degrad_mIkb',
    'degrad_RnaA20',
    'degrad_A20',
    'prod_Ikb',
    'prod_mIkb_by_nNfk',
    'build_RnaA20',
    'build_A20',
    'shuttle_RnaA20',
    #
    'len_f_params'\
]

for idx,name in enumerate(param_names):
    exec('%s=%d'%(name,idx))