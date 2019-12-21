var_naems = [\
    'IKKn',
    'IKKa',
    'IKKi',
    'IKKIkBa',
    'IKKIkBaNFkB',
    'NFkB',
    'NFkBn',
    'A20',
    'A20t',
    'IkBa',
    'IkBan',
    'IkBat',
    'IkBaNFkB',
    'IkBanNFkBn',
    'cgent',
    #
    'len_f_vars'\
]

for idx,name in enumerate(var_naems):
    exec('%s=%d'%(name,idx))