var_names = [\
    'MAP2K',
    'MAPK',
    'MKP1RNA',
    'MKP1',
    'S',
    'FRET',
    #
    'len_f_vars'\
]

for idx,name in enumerate(var_names):
  exec('%s=%d'%(name,idx))