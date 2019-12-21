param_names = [\
    'CycT',
    'Va25',
    'Vi25',
    'Vawee',
    'Viwee',
    'kagwl',
    'kigwl',
    'kigwl_d',
    'kigwl_dd',
    'kaensa',
    'kiensa',
    'kas',
    'kdis',
    'Cdc25T',
    'Wee1T',
    'GwlT',
    'ENSAT',
    'PP2T',
    'k25_d',
    'k25_dd',
    'kwee_d',
    'kwee_dd',
    'RO',
    'OA', 
    #
    'len_f_params'\
]

for idx,name in enumerate(param_names):
    exec('%s=%d'%(name,idx))
