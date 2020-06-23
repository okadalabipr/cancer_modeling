NAMES = [
    'CycT',
    'Va25',
    'Vi25',
    'Vawee',
    'Viwee',
    'kagwl',
    'kigwl',
    'kigwl_d',
    'kigwl_dd',
    'kaensa',
    'kiensa',
    'kas',
    'kdis',
    'Cdc25T',
    'Wee1T',
    'GwlT',
    'ENSAT',
    'PP2T',
    'k25_d',
    'k25_dd',
    'kwee_d',
    'kwee_dd',
    'RO',
    'OA', 
]

for idx, name in enumerate(NAMES):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

NUM = len(NAMES)
