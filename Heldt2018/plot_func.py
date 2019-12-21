from matplotlib import pyplot as plt

def timecourse(sim):
    plt.figure(figsize=(10,5))
    plt.rcParams['font.size'] = 32
    plt.rcParams['axes.linewidth'] = 1.5
    plt.rcParams['lines.linewidth'] = 6

    plt.plot(sim.t,sim.CycA,color='slateblue',label='CycA')
    plt.plot(sim.t,sim.CycE,color='skyblue',label='CycE')
    plt.plot(sim.t,sim.active_RC,color='firebrick',label='aRC')
    plt.plot(sim.t,sim.P21_tot,color='limegreen',label='p21')

    plt.xlim(0,20)
    plt.xlabel('time from cytokinesis (h)')
    plt.ylim(0,2)
    plt.ylabel('rel. level (AU)')
    plt.xticks([0,5,10,15,20])
    plt.yticks([0,1,2])
    plt.legend(loc='upper left',frameon=False,fontsize=18)

    plt.savefig('CycA_CycE_aRC_p21level.png',bbox_inches='tight')