var_names = [\
    'IL13stimulation',
    'Rec',
    'Rec_i',
    'IL13_Rec',
    'p_IL13_Rec',
    'p_IL13_Rec_i',
    'JAK2',
    'pJAK2',
    'SHP1',
    'STAT5',
    'pSTAT5',
    'SOCS3mRNA',
    'DecoyR',
    'IL13_DecoyR',
    'SOCS3',
    'CD274mRNA',
    #
    'len_f_vars'\
]

for idx,name in enumerate(var_names):
    exec('%s=%d'%(name,idx))