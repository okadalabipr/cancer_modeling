param_names = [\
    'k0',
    'k1',
    'k2',
    'k3',
    'k4',
    'k5',
    'k6',
    'k7',
    'k8',
    'k9',
    'k10',
    'k11',
    'k12',
    #
    'len_f_params'\
]

for idx,name in enumerate(param_names):
  exec('%s=%d'%(name,idx))