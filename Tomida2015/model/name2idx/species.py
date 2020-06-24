NAMES = [
    'MAP2K',
    'MAPK',
    'MKP1RNA',
    'MKP1',
    'S',
    'FRET',
]

for idx, name in enumerate(NAMES):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

NUM = len(NAMES)