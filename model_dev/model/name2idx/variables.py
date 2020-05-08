var_names = [\
    """
    This is where you define the parameter/variable names of your model.
    """
]

for idx, name in enumerate(var_names):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

len_f_vars = len(var_names)