var_names = [
    'MPF',
    'Cdc25',
    'Wee1',
    'Gwl',
    'ENSAPt',
    'PP2',
]

for idx, name in enumerate(var_names):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

len_f_vars = len(var_names)