from .name2idx import parameters as C
from .name2idx import variables as V

def diffeq(y,t,*x):
	v = [0]*114
	
	#1 ∅ −→ EGFR
	v[1] = 2*x[C.EGFR_basal_activation]*(x[C.init_EGFR]**2) *x[C.pEGFR_degradation] \
            /(x[C.pEGFR_degradation] + x[C.init_RTKph]*x[C.pEGFR_phosphatase_binding]) + x[C.EGFR_ErbB2_basal_act]  \
            *x[C.init_EGFR]*x[C.pErbB12_degradation]/(x[C.pErbB12_degradation] + x[C.init_RTKph] \
            *x[C.pErbB12i_phosphatase])+ x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR]*x[C.init_ErbB3] \
            *x[C.pErbB13_degradation]/(x[C.pErbB13_degradation] + x[C.init_RTKph]*x[C.pErbB13i_phosphatase]) \
            + x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]*x[C.pMetEGFR_degradation] \
            /(x[C.pMetEGFR_degradation] + x[C.init_RTKph]*x[C.pMetEGFRi_phosphatase])
	
	#2 ∅ −→ ErbB2
	v[2] = 2*x[C.ErbB2_dimerize]*(x[C.init_ErbB2]**2) *x[C.pErbB2_degradation] \
            /(x[C.pErbB2_degradation] + x[C.init_RTKph]*x[C.pErbB2i_phosphatase]) + x[C.EGFR_ErbB2_basal_act] \
            *x[C.init_EGFR]*x[C.init_ErbB2]*x[C.pErbB12_degradation]/(x[C.pErbB12_degradation] \
            + x[C.init_RTKph]*x[C.pErbB12i_phosphatase]) + x[C.ErbB3_ErbB2_basal_act]*x[C.init_ErbB2] \
            *x[C.init_ErbB3]*x[C.pErbB32_degradation]/(x[C.pErbB32_degradation] + x[C.init_RTKph] \
            *x[C.pErbB32i_phosphatase])
	
	#3 ∅ −→ ErbB3
	v[3] = 2*x[C.ErbB3_basal_activation]*(x[C.init_ErbB3]**2) *x[C.pErbB3_degradation] \
            /(x[C.pErbB3_degradation] + x[C.init_RTKph]*x[C.pErbB3i_phosphatase]) + x[C.EGFR_ErbB3_basal_act] \
            *x[C.init_EGFR]*x[C.init_ErbB3]*x[C.pErbB13_degradation]/(x[C.pErbB13_degradation] + x[C.init_RTKph] \
            *x[C.pErbB13i_phosphatase]) + x[C.ErbB3_ErbB2_basal_act]*x[C.init_ErbB2]*x[C.init_ErbB3] \
            *x[C.pErbB32_degradation]/(x[C.pErbB32_degradation] + x[C.init_RTKph]*x[C.pErbB32i_phosphatase]) \
            + x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3]*x[C.pMetErbB3_degradation] \
            /(x[C.pMetErbB3_degradation] + x[C.init_RTKph]*x[C.pMetErbB3i_phosphatase])
	
	#4 ∅ −→ IGF1R
	v[4] = 2*x[C.IGF1R_basal_activation]*(x[C.init_IGF1R]**2) *x[C.pIGF1R_degradation] \
            /(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase])
	
	#5 ∅ −→ Met
	v[5] = 2*x[C.Met_basal_act]*(x[C.init_Met]**2) *x[C.pMet_degradation]/(x[C.pMet_degradation] \
            + x[C.init_RTKph]*x[C.pMeti_phosphatase]) + x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met] \
            *x[C.pMetEGFR_degradation]/(x[C.pMetEGFR_degradation] + x[C.init_RTKph]*x[C.pMetEGFRi_phosphatase]) \
            + x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3]*x[C.pMetErbB3_degradation] \
            /(x[C.pMetErbB3_degradation] + x[C.init_RTKph]*x[C.pMetErbB3i_phosphatase])
	
	#6 dose EGF + EGFR −→ EGFR EGF
	v[6] = x[C.EGFR_lig_binding]*y[V.dose_EGF]*y[V.EGFR]
	
	#7 EGFR EGF −→ dose EGF + EGFR
	v[7] = x[C.EGF_kD]*y[V.EGFR_EGF]*x[C.EGFR_lig_binding]

	#test8 dose BTC + EGFR −→ EGFR BTC
	v[8] = y[V.EGFR]*x[C.EGFR_BTC_binding]*y[V.dose_BTC]

	#test9 EGFR BTC −→ dose BTC + EGFR
	v[9] = y[V.EGFR_BTC]*x[C.EGFR_BTC_binding]*x[C.EGF_kD]
	
	#10 dose HRG + ErbB3 −→ ErbB3 HRG
	v[10] = x[C.ErbB3_lig_binding]*y[V.dose_HRG]*y[V.ErbB3]
	
	#11 ErbB3 HRG −→ dose HRG + ErbB3
	v[11] = y[V.ErbB3_HRG]*x[C.ErbB3_lig_binding]*x[C.HRG_kD]
	
	#12 dose IGF1 + IGF1R −→ IGF1R IGF1
	v[12] = x[C.IGF1R_lig_binding]*y[V.dose_IGF1]*y[V.IGF1R]
	
	#13 IGF1R IGF1 −→ dose IGF1 + IGF1R
	v[13] = x[C.IGF1_kD]*y[V.IGF1R_IGF1]*x[C.IGF1R_lig_binding]
	
	#14 dose HGF + Met −→ Met HGF
	v[14] = x[C.Met_lig_binding]*y[V.dose_HGF]*y[V.Met]
	
	#15 Met HGF −→ dose HGF + Met
	v[15] = x[C.HGF_kD]*y[V.Met_HGF]*x[C.Met_lig_binding]
	
	#16 2·EGFR EGF −→ pEGFRd
	v[16] = x[C.EGFR_dimerize]*(y[V.EGFR_EGF]**2)

	#test17 2·EGFR BTC −→ pEGFRd
	v[17] = (y[V.EGFR_BTC]**2)*x[C.EGFR_BTC_dimerize]
	
	#18 2·ErbB2 −→ pErbB2
	v[18] = x[C.ErbB2_dimerize]*(y[V.ErbB2]**2)
	
	#19 2·ErbB3 HRG −→ pErbB3d
	v[19] = x[C.ErbB3_dimerize]*(y[V.ErbB3_HRG]**2)
	
	#20 2·IGF1R IGF1 −→ pIGF1Rd
	v[20] = x[C.IGF1R_dimerize]*(y[V.IGF1R_IGF1]**2)
	
	#21 EGFR EGF + ErbB2 −→ pErbB12
	v[21] = x[C.EGFR_ErbB2_dimerize]*y[V.EGFR_EGF]*y[V.ErbB2]

	#test22 EGFR BTC + ErbB2 −→ pErbB12
	v[22] = y[V.EGFR_BTC]*x[C.EGFR_ErbB2_BTC_dimerize]*y[V.ErbB2]
	
	#23 EGFR EGF + ErbB3 HRG −→ pErbB13
	v[23] = x[C.EGFR_ErbB3_dimerize]*y[V.EGFR_EGF]*y[V.ErbB3_HRG]

	#test24 EGFR BTC + ErbB3 HRG −→ pErbB13
	v[24] = y[V.EGFR_BTC]*x[C.EGFR_ErbB3_BTC_dimerize]*y[V.ErbB3_HRG]

	#test25 EGFR BTC + ErbB3 −→ pErbB13
	v[25] = y[V.EGFR_BTC]*x[C.EGFR_ErbB3_dimerize_noHRG]*y[V.ErbB3]
	
	#26 ErbB2 + ErbB3 HRG −→ pErbB32
	v[26] = x[C.ErbB2_ErbB3_dimerize]*y[V.ErbB2]*y[V.ErbB3_HRG]

	#27 2·Met HGF −→ pMetd
	v[27] = x[C.Met_dimerize]*(y[V.Met_HGF]**2)

	#28 ErbB3 HRG + Met −→ pMetErbB3
	v[28] = x[C.Met_ErbB3_dimerize]*y[V.ErbB3_HRG]*y[V.Met]
	
	#29 ErbB3 HRG + Met HGF −→ pMetErbB3
	v[29] = x[C.Met_lig_ErbB3_dimerize]*y[V.ErbB3_HRG]*y[V.Met_HGF]
	
	#30 EGFR EGF + Met HGF −→ pMetEGFR
	v[30] = x[C.Met_EGFR_dimerize]*y[V.EGFR_EGF]*y[V.Met_HGF]

	#test31 EGFR BTC + Met HGF −→ pMetEGFR
	v[31] = y[V.EGFR_BTC]*x[C.Met_EGFR_BTC_dimerize]*y[V.Met_HGF]

	#32 2·EGFR −→ pEGFRd
	v[32] = x[C.EGFR_basal_activation]*(y[V.EGFR]**2)

	#33 2·ErbB3 −→ pErbB3d
	v[33] = x[C.ErbB3_basal_activation]*(y[V.ErbB3]**2)
	
	#34 2·IGF1R −→ pIGF1Rd
	v[34] = x[C.IGF1R_basal_activation]*(y[V.IGF1R]**2)

	#35 EGFR + ErbB2 −→ pErbB12
	v[35] = x[C.EGFR_ErbB2_basal_act]*y[V.EGFR]*y[V.ErbB2]

	#36 EGFR + ErbB3 −→ pErbB13
	v[36] = x[C.EGFR_ErbB3_basal_act]*y[V.EGFR]*y[V.ErbB3]

	#37 ErbB2 + ErbB3 −→ pErbB32
	v[37] = x[C.ErbB3_ErbB2_basal_act]*y[V.ErbB2]*y[V.ErbB3]

	#38 ErbB3 + Met −→ pMetErbB3
	v[38] = x[C.Met_ErbB3_basal_act]*y[V.ErbB3]*y[V.Met]
	
	#39 2·Met −→ pMetd
	v[39] = x[C.Met_basal_act]*(y[V.Met]**2)
	
	#40 EGFR + Met −→ pMetEGFR
	v[40] = x[C.Met_EGFR_basal_act]*y[V.EGFR]*y[V.Met]
	
	#41 pEGFRd −→ pEGFRi
	v[41] = x[C.pEGFR_internalize]*y[V.pEGFRd]
	
	#42 pEGFRi −→ ∅
	v[42] = x[C.pEGFR_degradation]*y[V.pEGFRi]
	
	#43 RTKph + pEGFRi −→ pEGFRi ph
	v[43] = x[C.pEGFR_phosphatase_binding]*y[V.RTKph]*y[V.pEGFRi]
	
	#44 pEGFRi ph −→ RTKph + 2·EGFRi
	v[44] = x[C.pEGFRi_dephosph]*y[V.pEGFRi_ph]
	
	#45 EGFRi −→ EGFR
	v[45] = x[C.EGFR_basal_recycle]*y[V.EGFRi]
	
	#46 pErbB2 −→ pErbB2i
	v[46] = x[C.pErbB2_internalize]*y[V.pErbB2]
	
	#47 RTKph + pErbB2i −→ pErbB2i ph
	v[47] = x[C.pErbB2i_phosphatase]*y[V.RTKph]*y[V.pErbB2i]
	
	#48 pErbB2i ph −→ RTKph + 2·ErbB2i
	v[48] = x[C.pErbB2i_dephosph]*y[V.pErbB2i_ph]
	
	#49 pErbB2i −→ ∅
	v[49] = x[C.pErbB2_degradation]*y[V.pErbB2i]
	
	#50 ErbB2i −→ ErbB2
	v[50] = x[C.ErbB2_recycle]*y[V.ErbB2i]

	#51 pErbB3d −→ pErbB3i
	v[51] = x[C.pErbB3_internalize]*y[V.pErbB3d]

	#52 pErbB3i −→ ∅
	v[52] = x[C.pErbB3_degradation]*y[V.pErbB3i]

	#53 RTKph + pErbB3i −→ pErbB3i ph
	v[53] = x[C.pErbB3i_phosphatase]*y[V.RTKph]*y[V.pErbB3i]

	#54 pErbB3i ph −→ RTKph + 2·ErbB3i
	v[54] = x[C.pErbB3i_dephosph]*y[V.pErbB3i_ph]

	#55 ErbB3i −→ ErbB3
	v[55] = x[C.ErbB3_basal_recycle]*y[V.ErbB3i]

	#56 pIGF1Rd −→ pIGF1Ri
	v[56] = x[C.pIGF1R_internalize]*y[V.pIGF1Rd]

	#57 pIGF1Ri −→ ∅
	v[57] = x[C.pIGF1R_degradation]*y[V.pIGF1Ri]

	#58 RTKph + pIGF1Ri −→ pIGF1Ri ph
	v[58] = x[C.pIGF1Ri_phosphatase]*y[V.RTKph]*y[V.pIGF1Ri]

	#59 pIGF1Ri ph −→ RTKph + 2·IGF1Ri
	v[59] = x[C.pIGF1Ri_dephosph]*y[V.pIGF1Ri_ph]

	#60 IGF1Ri −→ IGF1R
	v[60] = x[C.IGF1R_basal_recycle]*y[V.IGF1Ri]

	#61 pErbB12 −→ pErbB12i
	v[61] = x[C.pErbB12_internalize]*y[V.pErbB12]

	#62 pErbB12i −→ ∅
	v[62] = x[C.pErbB12_degradation]*y[V.pErbB12i]

	#63 RTKph + pErbB12i −→ pErbB12i ph
	v[63] = x[C.pErbB12i_phosphatase]*y[V.RTKph]*y[V.pErbB12i]

	#64 pErbB12i ph −→ RTKph + EGFRi + ErbB2i
	v[64] = x[C.pErbB12i_dephosph]*y[V.pErbB12i_ph]

	#65 pErbB32 −→ pErbB32i
	v[65] = x[C.pErbB32_internalize]*y[V.pErbB32]

	#66 pErbB32i −→ ∅
	v[66] = x[C.pErbB32_degradation]*y[V.pErbB32i]

	#67 RTKph + pErbB32i −→ pErbB32i ph
	v[67] = x[C.pErbB32i_phosphatase]*y[V.RTKph]*y[V.pErbB32i]

	#68 pErbB32i ph −→ RTKph + ErbB2i + ErbB3i
	v[68] = x[C.pErbB32i_dephosph]*y[V.pErbB32i_ph]

	#69 pErbB13 −→ pErbB13i
	v[69] = x[C.pErbB13_internalize]*y[V.pErbB13]

	#70 pErbB13i −→ ∅
	v[70] = x[C.pErbB13_degradation]*y[V.pErbB13i]

	#71 RTKph + pErbB13i −→ pErbB13i ph
	v[71] = x[C.pErbB13i_phosphatase]*y[V.RTKph]*y[V.pErbB13i]

	#72 pErbB13i ph −→ RTKph + EGFRi + ErbB3i
	v[72] = x[C.pErbB13i_dephosph]*y[V.pErbB13i_ph]

	#73 pMetd −→ pMeti
	v[73] = x[C.pMet_internalize]*y[V.pMetd]

	#74 pMeti −→ ∅
	v[74] = x[C.pMet_degradation]*y[V.pMeti]

	#75 RTKph + pMeti −→ pMeti ph
	v[75] = x[C.pMeti_phosphatase]*y[V.RTKph]*y[V.pMeti]

	#76 pMeti ph −→ RTKph + 2·Meti
	v[76] = x[C.pMeti_dephosph]*y[V.pMeti_ph]

	#77 Meti −→ Met
	v[77] = x[C.Met_recycle]*y[V.Meti]

	#78 pMetErbB3 −→ pMetErbB3i
	v[78] = x[C.pMetErbB3_internalize]*y[V.pMetErbB3]

	#79 pMetErbB3i −→ ∅
	v[79] = x[C.pMetErbB3_degradation]*y[V.pMetErbB3i]

	#80 RTKph + pMetErbB3i −→ pMetErbB3i ph
	v[80] = x[C.pMetErbB3i_phosphatase]*y[V.RTKph]*y[V.pMetErbB3i]

	#81 pMetErbB3i ph −→ RTKph + ErbB3i + Meti
	v[81] = x[C.pMetErbB3i_dephosph]*y[V.pMetErbB3i_ph]

	#82 pMetEGFR −→ pMetEGFRi
	v[82] = x[C.pMetEGFR_internalize]*y[V.pMetEGFR]

	#83 pMetEGFRi −→ ∅
	v[83] = x[C.pMetEGFR_degradation]*y[V.pMetEGFRi]

	#84 RTKph + pMetEGFRi −→ pMetEGFRi ph
	v[84] = x[C.pMetEGFRi_phosphatase]*y[V.RTKph]*y[V.pMetEGFRi]

	#85 pMetEGFRi ph −→ RTKph + EGFRi + Meti
	v[85] = x[C.pMetEGFRi_dephosph]*y[V.pMetEGFRi_ph]
	
	#86 MEK -pEGFRd,pERK→ pMEK
	v[86] = y[V.MEK]*x[C.MEK_phosphorylation_pEGFR]*y[V.pEGFRd]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR] \
            *x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act] \
            *x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR] \
            *x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize] + x[C.AKT_activation_pMetErbB3] \
            *x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3]/x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation] \
            *(x[C.feedback_pS6K1]*x[C.init_pS6K1] + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	
	#87 MEK -pErbB12,pERK→  pMEK
	v[87] = y[V.MEK]*x[C.MEK_phosphorylation_pErbB12]*y[V.pErbB12]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase])  \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR] \
            *x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act] \
            *x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR] \
            *x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize] + x[C.AKT_activation_pMetErbB3] \
            *x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3]/x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation] \
            *(x[C.feedback_pS6K1]*x[C.init_pS6K1] + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	
	#88 MEK -pErbB13,pERK→  pMEK
	v[88] = y[V.MEK]*x[C.MEK_phosphorylation_pErbB13]*y[V.pErbB13]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR] \
            *x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act] \
            *x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR] \
            *x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize]  \
            + x[C.AKT_activation_pMetErbB3]*x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3] \
            /x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation]*(x[C.feedback_pS6K1]*x[C.init_pS6K1] \
            + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	
	#89 MEK -pErbB32,pERK→ pMEK
	v[89] = y[V.MEK]*x[C.MEK_phosphorylation_pErbB32]*y[V.pErbB32]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR] \
             *x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act] \
             *x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR] \
             *x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize] \
            + x[C.AKT_activation_pMetErbB3]*x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3] \
            /x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation]*(x[C.feedback_pS6K1]*x[C.init_pS6K1] \
            + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	
	#90 MEK -pMetd,pERK→ pMEK
	v[90] = y[V.MEK]*x[C.MEK_phosphorylation_pMetd]*y[V.pMetd]/(x[C.feedback_pERK]*y[V.pERK] \
            + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation]*(x[C.init_EGFR]**2) \
            /x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation]*(x[C.init_IGF1R]**2) \
            /x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2)/x[C.pMet_internalize] \
            + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation]*(x[C.init_IGF1R]**2) \
            /(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) + x[C.AKT_activation_pErbB12] \
            *x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2]/x[C.pErbB12_internalize] \
            + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR]*x[C.init_ErbB3] \
            /x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act]*x[C.init_ErbB2] \
            *x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR]*x[C.Met_EGFR_basal_act] \
            *x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize] + x[C.AKT_activation_pMetErbB3] \
            *x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3]/x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation] \
            *(x[C.feedback_pS6K1]*x[C.init_pS6K1] + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	
	#91 MEK -pMetEGFR,pERK→ pMEK
	v[91] = y[V.MEK]*x[C.MEK_phosphorylation_pMetEGFR]*y[V.pMetEGFR]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase])  \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR] \
            *x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act] \
            *x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR] \
            *x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize] \
            + x[C.AKT_activation_pMetErbB3]*x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3] \
            /x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation]*(x[C.feedback_pS6K1]*x[C.init_pS6K1] \
            + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	
	#92 MEK -pIGF1Rd,pERK→ pMEK
	v[92] = y[V.MEK]*x[C.MEK_phosphorylation_pIGF1R]*y[V.pIGF1Rd]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR] \
            *x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act] \
            *x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR] \
            *x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize] \
            + x[C.AKT_activation_pMetErbB3]*x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3] \
            /x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation]*(x[C.feedback_pS6K1]*x[C.init_pS6K1] \
            + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	
	#93 MEK -pMetErbB3,pERK→ pMEK
	v[93] = y[V.MEK]*x[C.MEK_phosphorylation_pMetErbB3]*y[V.pMetErbB3]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act] \
            *x[C.init_EGFR]*x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32] \
            *x[C.ErbB3_ErbB2_basal_act]*x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] \
            + x[C.AKT_activation_pMetEGFR]*x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met] \
            /x[C.pMetEGFR_internalize] + x[C.AKT_activation_pMetErbB3]*x[C.Met_ErbB3_basal_act] \
            *x[C.init_Met]*x[C.init_ErbB3]/x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation] \
            *(x[C.feedback_pS6K1]*x[C.init_pS6K1] + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	
	#94 MEK -pIGF1Ri,pERK→ pMEK
	v[94] = y[V.MEK]*x[C.MEK_internIGF1R_effect]*x[C.MEK_phosphorylation_pIGF1R] \
            *y[V.pIGF1Ri]/(x[C.feedback_pERK]*y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR] \
            *x[C.EGFR_basal_activation]*(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R] \
            *x[C.IGF1R_basal_activation]*(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd] \
            *x[C.Met_basal_act]*(x[C.init_Met]**2)/x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R] \
            *x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation]*(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] \
            + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act] \
            *x[C.init_EGFR]*x[C.init_ErbB2]/x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13] \
            *x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR]*x[C.init_ErbB3]/x[C.pErbB13_internalize] \
            + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act]*x[C.init_ErbB2]*x[C.init_ErbB3] \
            /x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR]*x[C.Met_EGFR_basal_act]*x[C.init_EGFR] \
            *x[C.init_Met]/x[C.pMetEGFR_internalize] + x[C.AKT_activation_pMetErbB3]*x[C.Met_ErbB3_basal_act] \
            *x[C.init_Met]*x[C.init_ErbB3]/x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation]*(x[C.feedback_pS6K1] \
            *x[C.init_pS6K1] + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	
	#95 pMEK −→ MEK
	v[95] = x[C.pMEK_dephosphorylation]*y[V.pMEK]
	
	#96 ERK -pMEK→ pERK
	v[96] = y[V.ERK]*x[C.ERK_phosphorylation_pMEK]*y[V.pMEK]
	
	#97 pERK −→ ERK
	v[97] = x[C.pERK_dephosphorylation]*y[V.pERK]
	
	#98 AKT -pEGFRd,pERK,pS6K1→ pAKT
	v[98] = y[V.AKT]*x[C.AKT_activation_pEGFR]*y[V.pEGFRd]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	
	#99 AKT -pErbB12,pERK,pS6K1→ pAKT
	v[99] = y[V.AKT]*x[C.AKT_activation_pErbB12]*y[V.pErbB12]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	
	#100 AKT -pErbB13,pERK,pS6K1→ pAKT
	v[100] = y[V.AKT]*x[C.AKT_activation_pErbB13]*y[V.pErbB13]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	
	#101 AKT -pErbB32, pERK,pS6K1→ pAKT
	v[101] = y[V.AKT]*x[C.AKT_activation_pErbB32]*y[V.pErbB32]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	
	#102 AKT -pMetEGFR,pERK,pS6K1→ pAKT
	v[102] = y[V.AKT]*x[C.AKT_activation_pMetEGFR]*y[V.pMetEGFR]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	
	#103 AKT -pMetd,pERK,pS6K1→ pAKT
	v[103] = y[V.AKT]*x[C.AKT_activation_pMetd]*y[V.pMetd]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	
	#104 AKT -pIGF1Rd,pERK,pS6K1→ pAKT
	v[104] = y[V.AKT]*x[C.AKT_activation_pIGF1R]*y[V.pIGF1Rd]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	
	#105 AKT -pMetErbB3,pERK,pS6K1→ pAKT
	v[105] = y[V.AKT]*x[C.AKT_activation_pMetErbB3]*y[V.pMetErbB3]/(x[C.feedback_pERK_on_AKT] \
            *y[V.pERK] + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	
	#106 AKT −pIGF1Ri,pERK,pS6K1→ pAKT
	v[106] = y[V.AKT]*x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*y[V.pIGF1Ri] \
            /(x[C.feedback_pERK_on_AKT]*y[V.pERK] + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	
	#107 pAKT −→ AKT
	v[107] = x[C.pAKT_deactivation]*y[V.pAKT]
	
	#108 -S6K1-pAKT→ pS6K1
	v[108] = y[V.S6K1]*x[C.S6K1_phosphorylation_pAKT]*y[V.pAKT]
	
	#109 S6K1-pERK→ pS6K1
	v[109] = y[V.S6K1]*x[C.S6K1_phosphorylation_pERK]*y[V.pERK]
	
	#109 pS6K1 −→ S6K1
	v[110] = x[C.pS6K1_dephosphorylation]*y[V.pS6K1]
	
	#111 S6 -pS6K1→ pS6
	v[111] = y[V.S6]*x[C.S6_phosphorylation_pS6K1]*y[V.pS6K1]
	
	#112 S6 pERK→ pS6
	v[112] = y[V.S6]*x[C.S6_phosphorylation_pERK]*y[V.pERK]
	
	#113 pS6 −→ S6
	v[113] = x[C.pS6_dephosphorylation]*y[V.pS6]




	dydt = [0]*V.len_f_vars
	dydt[V.dose_EGF] = - v[6] + v[7]
	dydt[V.dose_HGF] = - v[14] + v[15]
	dydt[V.RTKph] = - v[43] + v[44] - v[47] + v[48] - v[53] + v[54] - v[58] + v[59] \
					- v[63] + v[64] - v[67] + v[68] - v[71] + v[72] - v[75] + v[76] \
					- v[80] + v[81] - v[84] + v[85]
	dydt[V.dose_IGF1] = - v[12] + v[13]
	dydt[V.dose_HRG] = - v[10] + v[11]
	dydt[V.dose_BTC] = -v[8] + v[9]
	dydt[V.EGFR] = v[1] - v[6] + v[7] - 2.0*v[32] - v[35] - v[36] - v[40] + v[45]
	dydt[V.EGFR_EGF] = v[6] - v[7] - 2.0*v[16] - v[21] - v[23] - v[30]
	dydt[V.EGFR_BTC] = v[8] - v[9] - 2.0*v[17] - v[22] - v[24] - v[25] - v[31]
	dydt[V.pEGFRd] = v[16] + v[32] - v[41]
	dydt[V.pEGFRi] = v[41] - v[42] - v[43]
	dydt[V.pEGFRi_ph] = v[43] - v[44]
	dydt[V.EGFRi] = 2.0*v[44] - v[45] + v[64] + v[72] + v[85]
	dydt[V.ErbB2] = v[2] - 2.0*v[18] - v[21] - v[26] - v[35] - v[37] + v[50]
	dydt[V.pErbB2] = v[18] - v[46]
	dydt[V.pErbB2i] = v[46] - v[47] - v[49]
	dydt[V.ErbB2i] = 2.0*v[48] - v[50] + v[64] + v[68]
	dydt[V.pErbB2i_ph] = v[47] - v[48]
	dydt[V.pErbB12] = v[21] + v[35] - v[61]
	dydt[V.pErbB12i] = v[61] - v[62] - v[63]
	dydt[V.pErbB12i_ph] = v[63] - v[64]
	dydt[V.ErbB3] = v[3] - v[10] + v[11] - 2.0*v[33] - v[36] - v[37] - v[38] + v[55]
	dydt[V.ErbB3_HRG] = v[10] - v[11] - 2.0*v[19] - v[23] - v[26] - v[28] - v[29]
	dydt[V.pErbB3d] = v[19] + v[33] - v[51]
	dydt[V.pErbB3i] = v[51] - v[52] - v[53]
	dydt[V.pErbB3i_ph] = v[53] - v[54]
	dydt[V.ErbB3i] = 2.0*v[54] - v[55] + v[68] + v[72] + v[81]
	dydt[V.pErbB13] = v[23] + v[36] - v[69]
	dydt[V.pErbB13i] = v[69] - v[70] - v[71]
	dydt[V.pErbB13i_ph] = v[71] - v[72]
	dydt[V.pErbB32] = v[26] + v[37] - v[65]
	dydt[V.pErbB32i] = v[65] - v[66] - v[67]
	dydt[V.pErbB32i_ph] = v[67] - v[68]
	dydt[V.IGF1R] = v[4] - v[12] + v[13] - 2.0*v[34] + v[60]
	dydt[V.IGF1R_IGF1] = v[12] - v[13] - 2.0*v[20]
	dydt[V.pIGF1Rd] = v[20] + v[34] - v[56]
	dydt[V.pIGF1Ri] = v[56] - v[57] - v[58]
	dydt[V.pIGF1Ri_ph] = v[58] - v[59]
	dydt[V.IGF1Ri] = 2.0*v[59] - v[60]
	dydt[V.Met] = v[5] - v[14] + v[15] - v[28] - v[38] - 2.0*v[39] - v[40] + v[77]
	dydt[V.Met_HGF] = v[14] - v[15] - 2.0*v[27] - v[29] - v[30]
	dydt[V.pMetd] = v[27] + v[39] - v[73]
	dydt[V.pMeti] = v[73] - v[74] - v[75]
	dydt[V.pMeti_ph] = v[75] - v[76]
	dydt[V.Meti] = 2.0*v[76] - v[77] + v[81] + v[85]
	dydt[V.pMetErbB3] = v[28] + v[29] + v[38] - v[78]
	dydt[V.pMetErbB3i] = v[78] - v[79] - v[80]
	dydt[V.pMetErbB3i_ph] = v[80] - v[81]
	dydt[V.pMetEGFR] = v[30] + v[40] - v[82]
	dydt[V.pMetEGFRi] = v[82] - v[83] - v[84]
	dydt[V.pMetEGFRi_ph] = v[84] - v[85]
	dydt[V.MEK] = - v[86] - v[87] - v[88] - v[89] - v[90] - v[91] - v[92] - v[93] - v[94] + v[95]
	dydt[V.pMEK] = v[86] + v[87] + v[88] + v[89] + v[90] + v[91] + v[92] + v[93] + v[94] - v[95]
	dydt[V.ERK] = - v[96] + v[97]
	dydt[V.pERK] = v[96] - v[97]
	dydt[V.AKT] = - v[98] - v[99] - v[100] - v[101] - v[102] - v[103] - v[104] - v[105] - v[106] + v[107]
	dydt[V.pAKT] = v[98] + v[99] + v[100] + v[101] + v[102] + v[103] + v[104] + v[105] + v[106] - v[107]
	dydt[V.S6K1] = - v[108] - v[109] + v[110]
	dydt[V.pS6K1] = v[108] + v[109] - v[110]
	dydt[V.S6] = - v[111] - v[112] + v[113]
	dydt[V.pS6] = v[111] + v[112] - v[113]
	return dydt