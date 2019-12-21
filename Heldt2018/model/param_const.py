from .name2idx import parameters as C

def f_params():
    x = [0]*C.len_f_params

    x[C.Bg] = 0.05
    x[C.kSyE2f]=0.03
    x[C.kSyE2fE2f]=0.04
    x[C.jSyE2f]=0.2
    x[C.kAsRbE2f]=5.0
    x[C.kDsRbE2f]=0.005
    x[C.kDeE2f]=0.05
    x[C.kPhRbCd]=0.2
    x[C.kPhRbCe]=0.3
    x[C.kPhRbCa]=0.3
    x[C.kDpRb]=0.05
    x[C.kSyE1]=0.005
    x[C.kDeE1C1]=0.005
    x[C.kDeE1]=5.0E-4
    x[C.kPhC1]=0.0
    x[C.kPhC1Ce]=0.01
    x[C.kPhC1Ca]=1.0
    x[C.kDpC1]=0.05
    x[C.kAsE1C1]=10.0
    x[C.kDsE1C1]=0.01
    x[C.kSyP21]=0.002
    x[C.kSyP21P53]=0.008
    x[C.kDeP21]=0.0025
    x[C.kDeP21Cy]=0.007
    x[C.kDeP21aRc]=1.0
    x[C.kSyCe]=0.01
    x[C.kSyCa]=0.02
    x[C.kAsCyP21]=1.0
    x[C.kDsCyP21]=0.05
    x[C.kDeCe]=0.004
    x[C.kDeCa]=0.01
    x[C.kDeCeCa]=0.015
    x[C.kDeCaC1]=2.0
    x[C.kImPc]=0.003
    x[C.kExPc]=0.006
    x[C.kPhRc]=0.1
    x[C.kDpRc]=0.05
    x[C.jCy]=1.8
    x[C.n]=6.0
    x[C.kAsRcPc]=0.01
    x[C.kDsRcPc]=0.001
    x[C.kAsPcP21]=100.0
    x[C.kDsPcP21]=0.01
    x[C.kSyDna]=0.0093
    x[C.kSyP53]=0.05
    x[C.kDeP53]=0.05
    x[C.jP53]=0.01
    x[C.kGeDam]=0.001
    x[C.kGeDamArc]=0.012
    x[C.kReDam]=0.001
    x[C.kReDamP53]=0.005
    x[C.jDam]=0.5
    x[C.kSyPr]=0.01
    x[C.kDePr]=1.0E-4

    return x