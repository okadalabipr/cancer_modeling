var_names = [\
    """
    This is where you define the parameter/variable names of your model.
    """
    #
    'len_f_vars'\
]

for idx,name in enumerate(var_names):
    exec('%s=%d'%(name,idx))