var_names = [\
    
    'TGFb',
    'Rec',
    'TGFb_pRec',
    'S2',
    'S3',
    'S4',
    'ppS2_ppS2_ppS2',
    'ppS3_ppS3_ppS3',
    'S4_S4_S4',
    'pS2',
    'pS3',
    'ppS2',
    'ppS3',
    'ppS2_ppS2_S4',
    'ppS2_ppS2_ppS3',
    'ppS2_ppS3_ppS3',
    'ppS3_ppS3_S4',
    'ppS2_ppS3_S4',
    'ppS3_S4_S4',
    'ppS2_S4_S4',
    'gene',

    'len_f_vars'\
]

for idx,name in enumerate(var_names):
    exec('%s=%d'%(name,idx))