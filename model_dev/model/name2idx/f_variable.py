F_V = [\
    """
    This is where you define the parameter/variable names of your model.
    """
    #
    'len_f_vars'\
]

for i,name in enumerate(F_V):
    exec('%s=%d'%(name,i))