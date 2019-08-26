F_P = [\
    """
    This is where you define the parameter names of your model.
    """
    #
    'len_f_params'\
]

for i,name in enumerate(F_P):
    exec('%s=%d'%(name,i))
