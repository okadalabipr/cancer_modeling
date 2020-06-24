import numpy as np
from scipy.integrate import odeint

from .name2idx import C, V
from .set_model import diffeq, param_values, initial_values


class Simulation(object):
    t_start = 0
    t_end = 600
    h = 10000
    t = np.linspace(t_start, t_end, h)
    conditions = [
        'Ski', 'Skil', 'Dnmt3a',
        'Sox4', 'Jun', 'Smad7',
        'Klf10', 'Bmp4', 'Cxcl15',
        'Dusp5', 'Tgfa', 'Pdk4',
    ]

    x = param_values()
    y0 = initial_values()

    for j in range(4):
        if j == 0:
            y0[V.S2] = x[C.S2tot]
            y0[V.S3] = x[C.S3tot]
            y0[V.S4] = x[C.S4tot]
        elif j == 1:
            y0[V.S2] = 2*x[C.S2tot]
            y0[V.S3] = x[C.S3tot]
            y0[V.S4] = x[C.S4tot]
        elif j == 2:
            y0[V.S2] = x[C.S2tot]
            y0[V.S3] = 16*x[C.S3tot]
            y0[V.S4] = x[C.S4tot]
        elif j == 3:
            y0[V.S2] = x[C.S2tot]
            y0[V.S3] = x[C.S3tot]
            y0[V.S4] = 3*x[C.S3tot]

        for _, gene_name in enumerate(conditions):
            if gene_name == 'Ski':
                x[C.gene_turn] = x[C.Ski_turn]
                x[C.gene_act1] = x[C.Ski_act1]
                x[C.gene_act2] = x[C.Ski_act2]
                x[C.gene_act3] = x[C.Ski_act3]
                x[C.gene_inh1] = x[C.Ski_inh1]
                x[C.gene_inh2] = x[C.Ski_inh2]
                x[C.gene_inh3] = x[C.Ski_inh3]

                Y = odeint(diffeq, y0, t, args=tuple(x))
                if j == 0:
                    Ski_WT = np.log2(Y[:, V.gene])
                elif j == 1:
                    Ski_Smad2OE = np.log2(Y[:, V.gene])
                elif j == 2:
                    Ski_Smad3OE = np.log2(Y[:, V.gene])
                elif j == 3:
                    Ski_Smad4OE = np.log2(Y[:, V.gene])

            elif gene_name == 'Skil':
                x[C.gene_turn] = x[C.Skil_turn]
                x[C.gene_act1] = x[C.Skil_act1]
                x[C.gene_act2] = x[C.Skil_act2]
                x[C.gene_act3] = x[C.Skil_act3]
                x[C.gene_inh1] = x[C.Skil_inh1]
                x[C.gene_inh2] = x[C.Skil_inh2]
                x[C.gene_inh3] = x[C.Skil_inh3]

                Y = odeint(diffeq, y0, t, args=tuple(x))
                if j == 0:
                    Skil_WT = np.log2(Y[:, V.gene])
                elif j == 1:
                    Skil_Smad2OE = np.log2(Y[:, V.gene])
                elif j == 2:
                    Skil_Smad3OE = np.log2(Y[:, V.gene])
                elif j == 3:
                    Skil_Smad4OE = np.log2(Y[:, V.gene])

            elif gene_name == 'Dnmt3a':
                x[C.gene_turn] = x[C.Dnmt3a_turn]
                x[C.gene_act1] = x[C.Dnmt3a_act1]
                x[C.gene_act2] = x[C.Dnmt3a_act2]
                x[C.gene_act3] = x[C.Dnmt3a_act3]
                x[C.gene_inh1] = x[C.Dnmt3a_inh1]
                x[C.gene_inh2] = x[C.Dnmt3a_inh2]
                x[C.gene_inh3] = x[C.Dnmt3a_inh3]

                Y = odeint(diffeq, y0, t, args=tuple(x))
                if j == 0:
                    Dnmt3a_WT = np.log2(Y[:, V.gene])
                elif j == 1:
                    Dnmt3a_Smad2OE = np.log2(Y[:, V.gene])
                elif j == 2:
                    Dnmt3a_Smad3OE = np.log2(Y[:, V.gene])
                elif j == 3:
                    Dnmt3a_Smad4OE = np.log2(Y[:, V.gene])

            elif gene_name == 'Sox4':
                x[C.gene_turn] = x[C.Sox4_turn]
                x[C.gene_act1] = x[C.Sox4_act1]
                x[C.gene_act2] = x[C.Sox4_act2]
                x[C.gene_act3] = x[C.Sox4_act3]
                x[C.gene_inh1] = x[C.Sox4_inh1]
                x[C.gene_inh2] = x[C.Sox4_inh2]
                x[C.gene_inh3] = x[C.Sox4_inh3]

                Y = odeint(diffeq, y0, t, args=tuple(x))
                if j == 0:
                    Sox4_WT = np.log2(Y[:, V.gene])
                elif j == 1:
                    Sox4_Smad2OE = np.log2(Y[:, V.gene])
                elif j == 2:
                    Sox4_Smad3OE = np.log2(Y[:, V.gene])
                elif j == 3:
                    Sox4_Smad4OE = np.log2(Y[:, V.gene])

            elif gene_name == 'Jun':
                x[C.gene_turn] = x[C.Jun_turn]
                x[C.gene_act1] = x[C.Jun_act1]
                x[C.gene_act2] = x[C.Jun_act2]
                x[C.gene_act3] = x[C.Jun_act3]
                x[C.gene_inh1] = x[C.Jun_inh1]
                x[C.gene_inh2] = x[C.Jun_inh2]
                x[C.gene_inh3] = x[C.Jun_inh3]

                Y = odeint(diffeq, y0, t, args=tuple(x))
                if j == 0:
                    Jun_WT = np.log2(Y[:, V.gene])
                elif j == 1:
                    Jun_Smad2OE = np.log2(Y[:, V.gene])
                elif j == 2:
                    Jun_Smad3OE = np.log2(Y[:, V.gene])
                elif j == 3:
                    Jun_Smad4OE = np.log2(Y[:, V.gene])

            elif gene_name == 'Smad7':
                x[C.gene_turn] = x[C.Smad7_turn]
                x[C.gene_act1] = x[C.Smad7_act1]
                x[C.gene_act2] = x[C.Smad7_act2]
                x[C.gene_act3] = x[C.Smad7_act3]
                x[C.gene_inh1] = x[C.Smad7_inh1]
                x[C.gene_inh2] = x[C.Smad7_inh2]
                x[C.gene_inh3] = x[C.Smad7_inh3]

                Y = odeint(diffeq, y0, t, args=tuple(x))
                if j == 0:
                    Smad7_WT = np.log2(Y[:, V.gene])
                elif j == 1:
                    Smad7_Smad2OE = np.log2(Y[:, V.gene])
                elif j == 2:
                    Smad7_Smad3OE = np.log2(Y[:, V.gene])
                elif j == 3:
                    Smad7_Smad4OE = np.log2(Y[:, V.gene])

            elif gene_name == 'Klf10':
                x[C.gene_turn] = x[C.Klf10_turn]
                x[C.gene_act1] = x[C.Klf10_act1]
                x[C.gene_act2] = x[C.Klf10_act2]
                x[C.gene_act3] = x[C.Klf10_act3]
                x[C.gene_inh1] = x[C.Klf10_inh1]
                x[C.gene_inh2] = x[C.Klf10_inh2]
                x[C.gene_inh3] = x[C.Klf10_inh3]

                Y = odeint(diffeq, y0, t, args=tuple(x))
                if j == 0:
                    Klf10_WT = np.log2(Y[:, V.gene])
                elif j == 1:
                    Klf10_Smad2OE = np.log2(Y[:, V.gene])
                elif j == 2:
                    Klf10_Smad3OE = np.log2(Y[:, V.gene])
                elif j == 3:
                    Klf10_Smad4OE = np.log2(Y[:, V.gene])

            elif gene_name == 'Bmp4':
                x[C.gene_turn] = x[C.Bmp4_turn]
                x[C.gene_act1] = x[C.Bmp4_act1]
                x[C.gene_act2] = x[C.Bmp4_act2]
                x[C.gene_act3] = x[C.Bmp4_act3]
                x[C.gene_inh1] = x[C.Bmp4_inh1]
                x[C.gene_inh2] = x[C.Bmp4_inh2]
                x[C.gene_inh3] = x[C.Bmp4_inh3]

                Y = odeint(diffeq, y0, t, args=tuple(x))
                if j == 0:
                    Bmp4_WT = np.log2(Y[:, V.gene])
                elif j == 1:
                    Bmp4_Smad2OE = np.log2(Y[:, V.gene])
                elif j == 2:
                    Bmp4_Smad3OE = np.log2(Y[:, V.gene])
                elif j == 3:
                    Bmp4_Smad4OE = np.log2(Y[:, V.gene])

            elif gene_name == 'Cxcl15':
                x[C.gene_turn] = x[C.Cxcl15_turn]
                x[C.gene_act1] = x[C.Cxcl15_act1]
                x[C.gene_act2] = x[C.Cxcl15_act2]
                x[C.gene_act3] = x[C.Cxcl15_act3]
                x[C.gene_inh1] = x[C.Cxcl15_inh1]
                x[C.gene_inh2] = x[C.Cxcl15_inh2]
                x[C.gene_inh3] = x[C.Cxcl15_inh3]

                Y = odeint(diffeq, y0, t, args=tuple(x))
                if j == 0:
                    Cxcl15_WT = np.log2(Y[:, V.gene])
                elif j == 1:
                    Cxcl15_Smad2OE = np.log2(Y[:, V.gene])
                elif j == 2:
                    Cxcl15_Smad3OE = np.log2(Y[:, V.gene])
                elif j == 3:
                    Cxcl15_Smad4OE = np.log2(Y[:, V.gene])

            elif gene_name == 'Dusp5':
                x[C.gene_turn] = x[C.Dusp5_turn]
                x[C.gene_act1] = x[C.Dusp5_act1]
                x[C.gene_act2] = x[C.Dusp5_act2]
                x[C.gene_act3] = x[C.Dusp5_act3]
                x[C.gene_inh1] = x[C.Dusp5_inh1]
                x[C.gene_inh2] = x[C.Dusp5_inh2]
                x[C.gene_inh3] = x[C.Dusp5_inh3]

                Y = odeint(diffeq, y0, t, args=tuple(x))
                if j == 0:
                    Dusp5_WT = np.log2(Y[:, V.gene])
                elif j == 1:
                    Dusp5_Smad2OE = np.log2(Y[:, V.gene])
                elif j == 2:
                    Dusp5_Smad3OE = np.log2(Y[:, V.gene])
                elif j == 3:
                    Dusp5_Smad4OE = np.log2(Y[:, V.gene])

            elif gene_name == 'Tgfa':
                x[C.gene_turn] = x[C.Tgfa_turn]
                x[C.gene_act1] = x[C.Tgfa_act1]
                x[C.gene_act2] = x[C.Tgfa_act2]
                x[C.gene_act3] = x[C.Tgfa_act3]
                x[C.gene_inh1] = x[C.Tgfa_inh1]
                x[C.gene_inh2] = x[C.Tgfa_inh2]
                x[C.gene_inh3] = x[C.Tgfa_inh3]

                Y = odeint(diffeq, y0, t, args=tuple(x))
                if j == 0:
                    Tgfa_WT = np.log2(Y[:, V.gene])
                elif j == 1:
                    Tgfa_Smad2OE = np.log2(Y[:, V.gene])
                elif j == 2:
                    Tgfa_Smad3OE = np.log2(Y[:, V.gene])
                elif j == 3:
                    Tgfa_Smad4OE = np.log2(Y[:, V.gene])

            elif gene_name == 'Pdk4':
                x[C.gene_turn] = x[C.Pdk4_turn]
                x[C.gene_act1] = x[C.Pdk4_act1]
                x[C.gene_act2] = x[C.Pdk4_act2]
                x[C.gene_act3] = x[C.Pdk4_act3]
                x[C.gene_inh1] = x[C.Pdk4_inh1]
                x[C.gene_inh2] = x[C.Pdk4_inh2]
                x[C.gene_inh3] = x[C.Pdk4_inh3]

                Y = odeint(diffeq, y0, t, args=tuple(x))
                if j == 0:
                    Pdk4_WT = np.log2(Y[:, V.gene])
                elif j == 1:
                    Pdk4_Smad2OE = np.log2(Y[:, V.gene])
                elif j == 2:
                    Pdk4_Smad3OE = np.log2(Y[:, V.gene])
                elif j == 3:
                    Pdk4_Smad4OE = np.log2(Y[:, V.gene])
