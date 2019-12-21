from .name2idx import parameters as C

def f_params():
    x = [0]*C.len_f_params

    ## CYCE SYNTHESISx[C.DEGRADATION AND P27 BINDING/DISSOCIATION:
    x[C.kscyce]=0.003
    x[C.kdcyce]=0.001
    x[C.kdcycee]=0.0001
    x[C.kdcycea]=0.03
    x[C.kasse]=1
    x[C.kdise]=0.02
    ## CYCA SYNTHESISx[C.DEGRADATION AND P27 BINDING/DISSOCIATION:
    x[C.kscyca]=0.0025
    x[C.kdcyca]=0.002
    x[C.kdcycac1]=0.4
    x[C.kassa]=1
    x[C.kdisa]=0.02
    ## P27 SYNTHESIS AND DEGRADATION:
    x[C.ks27]=0.008
    x[C.kd27]=0.004
    x[C.kd27e]=2
    x[C.kd27a]=2
    ## EMI1 SYNTHESIS AND DEGRADATION:
    x[C.ksemi1]=0.003
    x[C.kdemi1]=0.001
    ## CDH1 REGULATION:
    x[C.Cdh1T]=1
    x[C.kacdh1]=0.02
    x[C.kicdh1e]=0.07
    x[C.kicdh1a]=0.2
    x[C.kasec]=2
    x[C.kdiec]=0.02
    ## SKP2 SYNTHESIS AND DEGRADATION:
    x[C.ksskp2]=0.004
    x[C.kdskp2]=0.002
    x[C.kdskp2c1]=0.2
    ## CDK INHIBITOR
    x[C.Inhibitor]=0

    return x