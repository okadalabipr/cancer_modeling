param_names = [
    ## CYCE SYNTHESISDEGRADATION AND P27 BINDING/DISSOCIATION:
    'kscyce',
    'kdcyce',
    'kdcycee',
    'kdcycea',
    'kasse',
    'kdise',
    ## CYCA SYNTHESISDEGRADATION AND P27 BINDING/DISSOCIATION:
    'kscyca',
    'kdcyca',
    'kdcycac1',
    'kassa',
    'kdisa',
    ## P27 SYNTHESIS AND DEGRADATION:
    'ks27',
    'kd27',
    'kd27e',
    'kd27a',
    ## EMI1 SYNTHESIS AND DEGRADATION:
    'ksemi1',
    'kdemi1',
    ## CDH1 REGULATION:
    'Cdh1T',
    'kacdh1',
    'kicdh1e',
    'kicdh1a',
    'kasec',
    'kdiec',
    ## SKP2 SYNTHESIS AND DEGRADATION:
    'ksskp2',
    'kdskp2',
    'kdskp2c1',
    ## CDK INHIBITOR
    'Inhibitor',
]

for idx, name in enumerate(param_names):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

len_f_params = len(param_names)