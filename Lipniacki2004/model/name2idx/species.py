NAMES = [
    'IKKn',
    'IKKa',
    'IKKi',
    'IKKIkBa',
    'IKKIkBaNFkB',
    'NFkB',
    'NFkBn',
    'A20',
    'A20t',
    'IkBa',
    'IkBan',
    'IkBat',
    'IkBaNFkB',
    'IkBanNFkBn',
    'cgent',
]

for idx, name in enumerate(NAMES):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

NUM = len(NAMES)