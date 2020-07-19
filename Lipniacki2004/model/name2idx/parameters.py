NAMES = [
    'TR',   # TNFα concentration
    'a1',   # IkBa2NFkB association
    'a2',   # IKKa–IkBa association
    't1',   # IKKajIkBa catalysis
    'a3',   # IKKa-(IkBajNF-kB) association
    't2',   # (IKKjIkBajNF-kB) catalysis
    'c1a',  # IkBa-inducible mRNA synthesis
    'c2a',  # IkBa-constitutive mRNA synthesis
    'c3a',  # IkBa mRNA degradation
    'c4a',  # IkBa translation rate
    'c5a',  # Spontaneous, free IkBa protein degradation
    'c6a',  # IkBa degradation (complexed to NF-kB)
    'c1',   # A20-inducible mRNA synthesis
    'c2',   # A20-constitutive mRNA synthesis
    'c3',   # A20 mRNA degradation
    'c4',   # A20 translation rate
    'c5',   # A20 protein degradation
    'k1',   # IKK activation rate caused by TNF
    'k2',   # IKK inactivation rate caused by A20
    'k3',   # IKK spontaneous inactivation rate
    'kprod',# IKKn production rate
    'kdeg', # IKKa, IKKn and IKKi degradation
    'kv',   # Cytoplasmic to nuclear volume
    'i1',   # NF-kB nuclear import
    'e2a',  # (IkBajNF-kBÞ nuclear export
    'i1a',  # IkBa nuclear import
    'e1a',  # IkBa nuclear export
    'c1c',  # cgen inducible mRNA synthesis
    'c2c',  # cgen constitutive mRNA synthesis
    'c3c',  # cgen mRNA degradation
]

for idx, name in enumerate(NAMES):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

NUM = len(NAMES)
