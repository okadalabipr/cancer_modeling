import numpy as np
from scipy.integrate import odeint

from .name2idx import C, V
from .set_model import diffeq, param_values, initial_values


class Simulation(object):
    t = range(121)
    conditions = [
        'EGF20',
        'EGF2',
        'PLCgP_transloc'
    ]

    totalShc = np.empty((len(t), len(conditions)))
    totalGrb2 = np.empty((len(t), len(conditions)))
    RSh = np.empty((len(t), len(conditions)))
    RGrb2 = np.empty((len(t), len(conditions)))
    totalSOS = np.empty((len(t), len(conditions)))
    ShGS = np.empty((len(t), len(conditions)))
    PLCg = np.empty((len(t), len(conditions)))

    x = param_values()
    y0 = initial_values()

    for i, condition in enumerate(conditions):
        if condition == 'EGF20': # 20nM
            pass
        elif condition == 'EGF2': # 2nM
            y0[V.EGF] = 68.
        elif condition == 'PLCgP_transloc': # Absence of the PLCγP translocation step
            y0[V.EGF] = 680.
            x[C.k25f] = 0.
            x[C.k25b] = 0.

        Y = odeint(diffeq, y0, t, args=tuple(x))

        totalShc[:, i] = Y[:, V.R_ShP] + Y[:, V.R_Sh_G] + Y[:, V.R_Sh_G_S] + \
                            Y[:, V.ShP] + Y[:, V.Sh_G] + Y[:, V.Sh_G_S]
        totalGrb2[:, i] = Y[:, V.R_Sh_G] + Y[:, V.Sh_G] + Y[:, V.R_Sh_G_S] + Y[:, V.Sh_G_S]
        RSh[:, i] = Y[:, V.R_ShP] + Y[:, V.R_Sh_G] + Y[:, V.R_Sh_G_S]
        RGrb2[:, i] = Y[:, V.R_G] + Y[:, V.R_G_S] + Y[:, V.R_Sh_G] + Y[:, V.R_Sh_G_S]
        totalSOS[:, i] = Y[:, V.R_G_S] + Y[:, V.R_Sh_G_S]
        ShGS[:, i] = Y[:, V.Sh_G_S]
        PLCg[:, i] = Y[:, V.R_PLP] + Y[:, V.PLCgP]