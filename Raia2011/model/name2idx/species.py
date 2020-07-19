NAMES = [
    'IL13stimulation',
    'Rec',
    'Rec_i',
    'IL13_Rec',
    'p_IL13_Rec',
    'p_IL13_Rec_i',
    'JAK2',
    'pJAK2',
    'SHP1',
    'STAT5',
    'pSTAT5',
    'SOCS3mRNA',
    'DecoyR',
    'IL13_DecoyR',
    'SOCS3',
    'CD274mRNA',
]

for idx, name in enumerate(NAMES):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

NUM = len(NAMES)