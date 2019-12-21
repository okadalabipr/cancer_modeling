var_names = [\
    'CycET',
    'CycAT',
    'p27T',
    'CycEp27',
    'CycAp27',
    'Cdh1dp',
    'Emi1T',
    'EmiC',
    'Cdh1',
    'Skp2',
    #
    'len_f_vars'\
]

for idx,name in enumerate(var_names):
  exec('%s=%d'%(name,idx))