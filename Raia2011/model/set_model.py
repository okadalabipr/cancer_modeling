from .name2idx import C, V


def diffeq(y, t, *x):
    dydt = [0] * V.NUM

    dydt[V.Rec] = - x[C.Kon_IL13Rec]*y[V.IL13stimulation]*y[V.Rec]*2.265 - x[C.Rec_intern]*y[V.Rec] + x[C.Rec_recycle]*y[V.Rec_i]
    dydt[V.Rec_i] = x[C.Rec_intern]*y[V.Rec] - x[C.Rec_recycle]*y[V.Rec_i]
    dydt[V.IL13_Rec] = x[C.Kon_IL13Rec]*2.265*y[V.IL13stimulation]*y[V.Rec] - x[C.Rec_phosphorylation]*y[V.IL13_Rec]*y[V.pJAK2]
    dydt[V.p_IL13_Rec] = x[C.Rec_phosphorylation]*y[V.IL13_Rec]*y[V.pJAK2] - x[C.pRec_intern]*y[V.p_IL13_Rec]
    dydt[V.p_IL13_Rec_i] = x[C.pRec_intern]*y[V.p_IL13_Rec] - x[C.pRec_degradation]*y[V.p_IL13_Rec_i]
    dydt[V.JAK2] = -x[C.JAK2_phosphorylation]*y[V.IL13_Rec]*y[V.JAK2]/(1+x[C.JAK2_p_inhibition]*y[V.SOCS3]) \
                   - x[C.JAK2_phosphorylation]*y[V.p_IL13_Rec]*y[V.JAK2]/(1+x[C.JAK2_p_inhibition]*y[V.SOCS3]) \
                   + x[C.pJAK2_dephosphorylation]*y[V.pJAK2]*y[V.SHP1]
    dydt[V.pJAK2] = x[C.JAK2_phosphorylation]*y[V.IL13_Rec]*y[V.JAK2]/(1+x[C.JAK2_p_inhibition]*y[V.SOCS3]) \
                    + x[C.JAK2_phosphorylation]*y[V.p_IL13_Rec]*y[V.JAK2]/(1+x[C.JAK2_p_inhibition]*y[V.SOCS3]) \
                    - x[C.pJAK2_dephosphorylation]*y[V.pJAK2]*y[V.SHP1]
    dydt[V.SHP1] = 0
    dydt[V.STAT5] = -x[C.STAT5_phosphorylation]*y[V.STAT5]*y[V.pJAK2] + x[C.pSTAT5_dephosphorylation]*y[V.pSTAT5]*y[V.SHP1]
    dydt[V.pSTAT5] = x[C.STAT5_phosphorylation]*y[V.STAT5]*y[V.pJAK2] - x[C.pSTAT5_dephosphorylation]*y[V.pSTAT5]*y[V.SHP1]
    dydt[V.SOCS3mRNA] = y[V.pSTAT5]*x[C.SOCS3mRNA_production]
    dydt[V.DecoyR] = -x[C.DecoyR_binding]*y[V.IL13stimulation]*y[V.DecoyR]*2.265
    dydt[V.IL13_DecoyR] = x[C.DecoyR_binding]*y[V.IL13stimulation]*y[V.DecoyR]*2.265
    dydt[V.SOCS3] = y[V.SOCS3mRNA]*x[C.SOCS3_translation]/(x[C.SOCS3_accumulation]+y[V.SOCS3mRNA]) \
                    - x[C.SOCS3_degradation]*y[V.SOCS3]
    y[V.CD274mRNA] = y[V.pSTAT5]*x[C.CD274mRNA_production]
    
    return dydt


def param_values():
    x = [0] * C.NUM

    x[C.Kon_IL13Rec] = 0.00341992
    x[C.Rec_phosphorylation] = 999.631
    x[C.pRec_intern] = 0.15254
    x[C.pRec_degradation] = 0.172928
    x[C.Rec_intern] = 0.103346
    x[C.Rec_recycle] = 0.00135598
    x[C.JAK2_phosphorylation] = 0.157057
    x[C.pJAK2_dephosphorylation] = 6.21906E-4
    x[C.STAT5_phosphorylation] = 0.0382596
    x[C.pSTAT5_dephosphorylation] = 3.43392E-4
    x[C.SOCS3mRNA_production] = 0.00215826
    x[C.DecoyR_binding] = 1.24391E-4
    x[C.JAK2_p_inhibition] = 0.0168268
    x[C.SOCS3_translation] = 11.9086
    x[C.SOCS3_accumulation] = 3.70803
    x[C.SOCS3_degradation] = 0.0429186
    x[C.CD274mRNA_production] = 8.21752E-5

    return x


def initial_values():
    y0 = [0] * V.NUM
    
    y0[V.Rec] = 1.3
    y0[V.Rec_i] = 113.194
    y0[V.JAK2] = 2.8
    y0[V.SHP1] = 91.0
    y0[V.STAT5] = 165.0
    y0[V.DecoyR] = 3.4

    return y0