param_names = [
    'k1f',
    'k1b',
    'k2f',
    'k2b',
    'k3f',
    'k3b',
    'V4',
    'K4',
    'k5f',
    'k5b',
    'k6f',
    'k6b',
    'k7f',
    'k7b',
    'V8',
    'K8',
    'k9f',
    'k9b',
    'k10f',
    'k10b',
    'k11f',
    'k11b',
    'k12f',
    'k12b',
    'k13f',
    'k13b',
    'k14f',
    'k14b',
    'k15f',
    'k15b',
    'V16',
    'K16',
    'k17f',
    'k17b',
    'k18f',
    'k18b',
    'k19f',
    'k19b',
    'k20f',
    'k20b',
    'k21f',
    'k21b',
    'k22f',
    'k22b',
    'k23f',
    'k23b',
    'k24f',
    'k24b',
    'k25f',
    'k25b',
]

for idx, name in enumerate(param_names):
    exec(
		'{} = {:d}'.format(
			name,idx
		)
	)

len_f_params = len(param_names)