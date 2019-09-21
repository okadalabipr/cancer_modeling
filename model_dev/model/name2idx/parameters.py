param_names = [\
    """
    This is where you define the parameter names of your model.
    """
    #
    'len_f_params'\
]

for idx,name in enumerate(param_names):
    exec('%s=%d'%(name,idx))
