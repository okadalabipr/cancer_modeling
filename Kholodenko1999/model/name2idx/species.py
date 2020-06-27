NAMES = [
    'EGF',
    'R',
    'Ra',
    'R2',
    'RP',
    'PLCg',
    'R_PL',
    'R_PLP',
    'PLCgP',
    'Grb2',
    'R_G',
    'SOS',
    'R_G_S',
    'G_S',
    'Shc',
    'R_Sh',
    'R_ShP',
    'ShP',
    'R_Sh_G',
    'Sh_G',
    'R_Sh_G_S',
    'Sh_G_S',
    'PLCgP_I',
]

for idx, name in enumerate(NAMES):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

NUM = len(NAMES)