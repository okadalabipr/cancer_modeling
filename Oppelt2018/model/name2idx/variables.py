var_names = [\
    'TNFR',
    'Ikk',
    'pIkk',
    'ppIkk',
    'iIkk',
    'NfkIkb',
    'NfkpIkb',
    'pNfkIkb',
    'pNfkpIkb',
    'pNfk',
    'Nfk',
    'pIkb',
    'Ikb',
    'mIkb',
    'nIkb',
    'pnNfk',
    'nNfk',
    'nNfkIkb',
    'RnaA20_1',
    'RnaA20',
    'A20',
    #
    'len_f_vars'\
]

for idx,name in enumerate(var_names):
    exec('%s=%d'%(name,idx))