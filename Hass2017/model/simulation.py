import numpy as np
from scipy.integrate import odeint

from .name2idx import C, V
from .set_model import diffeq, param_values, initial_values

class Simulation(object):
    t_start = 0
    t_end = 300
    h = 1000
    t = np.linspace(t_start,t_end,h)
    conditions = 5
    
    pEGFR_au = np.empty((len(t),conditions))
    pErbB2_au = np.empty((len(t),conditions))
    pErbB3_au = np.empty((len(t),conditions))
    pIGF1R_au = np.empty((len(t),conditions))
    pERK_au = np.empty((len(t),conditions))
    pAKT_au = np.empty((len(t),conditions))
    pS6_au = np.empty((len(t),conditions))

    x = param_values()
    y0 = initial_values()

    # Cell line H322M
    for i in range(conditions):
        if i==0: 
            y0[V.dose_EGF] = 0
            y0[V.dose_HGF] = 0
            y0[V.dose_IGF1] = 0
            y0[V.dose_HRG] = 0
        elif i==1:
            y0[V.dose_EGF] = 0.156*x[C.scale_Ligand]
            y0[V.dose_IGF1] = 0
            y0[V.dose_HRG] = 0
        elif i==2:
            y0[V.dose_EGF] = 0.625*x[C.scale_Ligand]
            y0[V.dose_HGF] = 0
            y0[V.dose_IGF1] = 0
            y0[V.dose_HRG] = 0
        elif i==3:
            y0[V.dose_EGF] = 2.5*x[C.scale_Ligand]
            y0[V.dose_HGF] = 0
            y0[V.dose_IGF1] = 0
            y0[V.dose_HRG] = 0
        elif i==4:
            y0[V.dose_EGF] = 10*x[C.scale_Ligand]
            y0[V.dose_HGF] = 0
            y0[V.dose_IGF1] = 0
            y0[V.dose_HRG] = 0
            
        Y = odeint(diffeq,y0,t,args=tuple(x))

        pEGFR =  2*Y[:,V.pEGFRd] + 2*Y[:,V.pEGFRi] + 2*Y[:,V.pEGFRi_ph] + Y[:,V.pErbB12] \
                + Y[:,V.pErbB12i] + Y[:,V.pErbB12i_ph] + Y[:,V.pErbB13] + Y[:,V.pErbB13i] \
                + Y[:,V.pErbB13i_ph] + Y[:,V.pMetEGFR] + Y[:,V.pMetEGFRi] + Y[:,V.pMetEGFRi_ph]
        pErbB2 = Y[:,V.pErbB12] + Y[:,V.pErbB12i] + Y[:,V.pErbB12i_ph] + 2*Y[:,V.pErbB2] + 2*Y[:,V.pErbB2i] \
                + 2*Y[:,V.pErbB2i_ph] + Y[:,V.pErbB32] + Y[:,V.pErbB32i] + Y[:,V.pErbB32i_ph]
        pErbB3 = Y[:,V.pErbB13] + Y[:,V.pErbB13i] + Y[:,V.pErbB13i_ph] + Y[:,V.pErbB32] \
                + Y[:,V.pErbB32i] + Y[:,V.pErbB32i_ph] + 2*Y[:,V.pErbB3d] + 2*Y[:,V.pErbB3i] \
                + 2*Y[:,V.pErbB3i_ph] + Y[:,V.pMetErbB3] + Y[:,V.pMetErbB3i] + Y[:,V.pMetErbB3i_ph]
        pERK = Y[:,V.pERK]
        pAKT = Y[:,V.pAKT]
        pS6 = Y[:,V.pS6]

        pEGFR_au[:,i] = np.log10(x[C.offset_pEGFR_CelllineH322M] + x[C.scale_pEGFR_CelllineH322M]*pEGFR)
        pErbB2_au[:,i] = np.log10(x[C.offset_pErbB2_CelllineH322M] + x[C.scale_pErbB2_CelllineH322M]*pErbB2)
        pErbB3_au[:,i] = np.log10(x[C.offset_pErbB3_CelllineH322M] + x[C.scale_pErbB3_CelllineH322M]*pErbB3)
        pERK_au[:,i] = np.log10(x[C.offset_pERK_CelllineH322M] + x[C.scale_pERK_CelllineH322M]*pERK)
        pAKT_au[:,i] = np.log10(x[C.offset_pAKT_CelllineH322M] + x[C.scale_pAKT_CelllineH322M]*pAKT)
        pS6_au[:,i] = np.log10(x[C.offset_pS6_CelllineH322M] + x[C.scale_pS6_CelllineH322M]*pS6)