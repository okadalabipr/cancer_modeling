NAMES = [
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

for idx, name in enumerate(NAMES):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

NUM = len(NAMES)