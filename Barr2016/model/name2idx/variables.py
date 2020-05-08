var_names = [
    'CycET',
    'CycAT',
    'p27T',
    'CycEp27',
    'CycAp27',
    'Cdh1dp',
    'Emi1T',
    'EmiC',
    'Cdh1',
    'Skp2',
]

for idx, name in enumerate(var_names):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

len_f_vars = len(var_names)