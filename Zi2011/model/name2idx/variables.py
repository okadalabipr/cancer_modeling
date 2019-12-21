var_names = [\
    'TGF_beta_ex', #x1
    'T1R_surf', #x2
    'T1R_endo', #x3
    'T2R_surf', #x4
    'T2R_endo', #x5
    'LRC_surf', #x6
    'LRC_endo', #x7
    'Smad2c', #x8
    'Smad2n', #x9
    'Smad4c', #x10
    'Smad4n', #x11
    'PSmad2c', #x12
    'PSmad2_PSmad2_c', #x13
    'PSmad2_PSmad4_c', #x14
    'PSmad2n', #x15
    'PSmad2_PSmad2_n', #x16
    'PSmad2_Smad4_n', #x17
    'TGF_beta_endo', #x18
    'TGF_beta_ns', #x19
    #
    'len_f_vars'\
]

for idx,name in enumerate(var_names):
    exec('%s=%d'%(name,idx))
