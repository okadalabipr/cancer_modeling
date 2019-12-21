from .name2idx import parameters as C
from .name2idx import variables as V

def diffeq(y,t,*x):

  dydt = [0]*V.len_f_vars

  '''Leloup et al.,Toward a detailed computational model for the mammalian circadian clock,PNAS(2003)'''

  dydt[V.MP] = x[C.cvsP]*(y[V.BN]**x[C.cn])/(x[C.cKAP]**x[C.cn]+y[V.BN]**x[C.cn]) - x[C.cvmP]*y[V.MP]/(x[C.cKmP]+y[V.MP]) - x[C.ckdmp]*y[V.MP]
  dydt[V.MC] = x[C.cvsC]*(y[V.BN]**x[C.cn])/(x[C.cKAC]**x[C.cn]+y[V.BN]**x[C.cn]) - x[C.cvmC]*y[V.MC]/(x[C.cKmC]+y[V.MC]) - x[C.ckdmc]*y[V.MC]
  dydt[V.MB] = x[C.cvsB]*(x[C.cKIB]**x[C.cm])/(x[C.cKIB]**x[C.cm]+y[V.BN]**x[C.cm]) - x[C.cvmB]*y[V.MB]/(x[C.cKmB]+y[V.MB]) - x[C.ckdmb]*y[V.MB]
  dydt[V.PC] = x[C.cksP]*y[V.MP] - x[C.cV1P]*y[V.PC]/(x[C.cKp]+y[V.PC]) + x[C.cV2P]*y[V.PCP]/(x[C.cKdp]+y[V.PCP]) + x[C.ck4]*y[V.PCC] - x[C.ck3]*y[V.PC]*y[V.CC] - x[C.ckdn]*y[V.PC]
  dydt[V.CC] = x[C.cksC]*y[V.MC] - x[C.cV1C]*y[V.CC]/(x[C.cKp]+y[V.CC]) + x[C.cV2C]*y[V.CCP]/(x[C.cKdp]+y[V.CCP]) + x[C.ck4]*y[V.PCC] - x[C.ck3]*y[V.PC]*y[V.CC] - x[C.ckdnc]*y[V.CC]
  dydt[V.PCP] = x[C.cV1P]*y[V.PC]/(x[C.cKp]+y[V.PC]) - x[C.cV2P]*y[V.PCP]/(x[C.cKdp]+y[V.PCP]) - x[C.cvdPC]*y[V.PCP]/(x[C.cKd]+y[V.PCP]) - x[C.ckdn]*y[V.PCP]
  dydt[V.CCP] = x[C.cV1C]*y[V.CC]/(x[C.cKp]+y[V.CC]) - x[C.cV2C]*y[V.CCP]/(x[C.cKdp]+y[V.CCP]) - x[C.cvdCC]*y[V.CCP]/(x[C.cKd]+y[V.CCP]) - x[C.ckdn]*y[V.CCP]
  dydt[V.PCC] = -x[C.cV1PC]*y[V.PCC]/(x[C.cKp]+y[V.PCC]) + x[C.cV2PC]*y[V.PCCP]/(x[C.cKdp]+y[V.PCCP]) - x[C.ck4]*y[V.PCC] + x[C.ck3]*y[V.PC]*y[V.CC] + x[C.ck2]*y[V.PCN] - x[C.ck1]*y[V.PCC] - x[C.ckdn]*y[V.PCC]
  dydt[V.PCN] = -x[C.cV3PC]*y[V.PCN]/(x[C.cKp]+y[V.PCN]) + x[C.cV4PC]*y[V.PCNP]/(x[C.cKdp]+y[V.PCNP]) - x[C.ck2]*y[V.PCN] + x[C.ck1]*y[V.PCC] - x[C.ck7]*y[V.BN]*y[V.PCN] + x[C.ck8]*y[V.IN] - x[C.ckdn]*y[V.PCN]
  dydt[V.PCCP] = x[C.cV1PC]*y[V.PCC]/(x[C.cKp]+y[V.PCC]) - x[C.cV2PC]*y[V.PCCP]/(x[C.cKdp]+y[V.PCCP]) - x[C.cvdPCC]*y[V.PCCP]/(x[C.cKd]+y[V.PCCP]) - x[C.ckdn]*y[V.PCCP]
  dydt[V.PCNP] = x[C.cV3PC]*y[V.PCN]/(x[C.cKp]+y[V.PCN]) - x[C.cV4PC]*y[V.PCNP]/(x[C.cKdp]+y[V.PCNP]) - x[C.cvdPCN]*y[V.PCNP]/(x[C.cKd]+y[V.PCNP]) - x[C.ckdn]*y[V.PCNP]
  dydt[V.BC] = x[C.cksB]*y[V.MB] - x[C.cV1B]*y[V.BC]/(x[C.cKp]+y[V.BC]) + x[C.cV2B]*y[V.BCP]/(x[C.cKdp]+y[V.BCP]) - x[C.ck5]*y[V.BC] + x[C.ck6]*y[V.BN] - x[C.ckdn]*y[V.BC]
  dydt[V.BCP] = x[C.cV1B]*y[V.BC]/(x[C.cKp]+y[V.BC]) - x[C.cV2B]*y[V.BCP]/(x[C.cKdp]+y[V.BCP]) - x[C.cvdBC]*y[V.BCP]/(x[C.cKd]+y[V.BCP]) - x[C.ckdn]*y[V.BCP]
  dydt[V.BN] = -x[C.cV3B]*y[V.BN]/(x[C.cKp]+y[V.BN]) + x[C.cV4B]*y[V.BNP]/(x[C.cKdp]+y[V.BNP]) + x[C.ck5]*y[V.BC] - x[C.ck6]*y[V.BN] - x[C.ck7]*y[V.BN]*y[V.PCN] + x[C.ck8]*y[V.IN] - x[C.ckdn]*y[V.BN]
  dydt[V.BNP] = x[C.cV3B]*y[V.BN]/(x[C.cKp]+y[V.BN]) - x[C.cV4B]*y[V.BNP]/(x[C.cKdp]+y[V.BNP]) - x[C.cvdBN]*y[V.BNP]/(x[C.cKd]+y[V.BNP]) - x[C.ckdn]*y[V.BNP]
  dydt[V.IN] = -x[C.ck8]*y[V.IN] + x[C.ck7]*y[V.BN]*y[V.PCN] - x[C.cvdIN]*y[V.IN]/(x[C.cKd]+y[V.IN]) - x[C.ckdn]*y[V.IN]

  return dydt