NAMES = [\
    """
    This is where you define the parameter names of your model.
    """
]

for idx, name in enumerate(NAMES):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

NUM = len(NAMES)
