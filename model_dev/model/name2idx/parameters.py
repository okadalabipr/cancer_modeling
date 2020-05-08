param_names = [\
    """
    This is where you define the parameter names of your model.
    """
]

for idx, name in enumerate(param_names):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

len_f_params = len(param_names)
