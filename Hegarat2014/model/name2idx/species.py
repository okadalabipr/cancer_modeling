NAMES = [
    'MPF',
    'Cdc25',
    'Wee1',
    'Gwl',
    'ENSAPt',
    'PP2',
]

for idx, name in enumerate(NAMES):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

NUM = len(NAMES)