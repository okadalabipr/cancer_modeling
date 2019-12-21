var_names = [
    'uRb',
    'tE2f',
    'E2f',
    'tE1',
    'tP21',
    'tCe',
    'tCa',
    'CeP21',
    'CaP21',
    'C1',
    'E1C1',
    'aPcna',
    'iPcna',
    'Rc',
    'pRc',
    'aRc',
    'iRc',
    'Dna',
    'P53',
    'Dam',
    'Pr',
    #
    'len_f_vars'\
]

for idx,name in enumerate(var_names):
  exec('%s=%d'%(name,idx))