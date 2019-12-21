var_names = [\
    'MPF',
    'Cdc25',
    'Wee1',
    'Gwl',
    'ENSAPt',
    'PP2',
    
    #
    'len_f_vars'\
]

for idx,name in enumerate(var_names):
    exec('%s=%d'%(name,idx))