var_names = [\
    'Ins',
    'pro_IRcom',
    'IRcom',
    'p1IRcom',
    'p2IRcom',
    'p1p2IRcom',
    'iAKT',
    'pAKT',
    'imTOR',
    'pmTOR',
    'iX',
    'pX',
    'iS6K',
    'pS6K',
    'iGSK3B',
    'pGSK3B',
    'iFoxO1',
    'pFoxO1',
    'G6Pase',
    #
    'len_f_vars'\
]

for idx,name in enumerate(var_names):
    exec('%s=%d'%(name,idx))
