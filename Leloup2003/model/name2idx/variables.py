var_names = [\
    #--- Leloup et al.,Toward a detailed computational model for the mammalian circadian clock,PNAS(2003) ---#
    'MP',
    'MC',
    'MB',
    'PC',
    'CC',
    'PCP',
    'CCP',
    'PCC',
    'PCN',
    'PCCP',
    'PCNP',
    'BC',
    'BCP',
    'BN',
    'BNP',
    'IN',
    #
    'len_f_vars'\
]

for idx,name in enumerate(var_names):
  exec('%s=%d'%(name,idx))