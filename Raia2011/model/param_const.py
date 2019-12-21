from .name2idx import parameters as C

def f_params():
    x = [0]*C.len_f_params

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