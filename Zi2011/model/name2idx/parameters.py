param_names = [\
    # Summary of the derived parameter values based on published models and experimental data
    'kdeg_T1R',
    'kdeg_T2R',
    'kdeg_LRC',
    'kdeg_TGF_beta',
    'kprod_T1R',
    'ki',
    'kr',
    'kimp_Smad2',
    'kexp_Smad2',
    'kimp_Smad4',
    'kexp_Smad4',
    'kimp_Smads',
    'koff_Smads',
    'kdepho_Smad2',
    # Statistical analysis of the estimated parameters
    'kprod_T2R',
    'ka_LRC',
    'kdiss_LRC',
    'klid',
    'kpho_Smad2',
    'kon_Smads',
    'kon_ns',
    'KD_ns',
    ##
    'len_f_params'\
]

for idx,name in enumerate(param_names):
    exec('%s=%d'%(name,idx))
