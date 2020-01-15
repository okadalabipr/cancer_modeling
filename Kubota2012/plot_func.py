import matplotlib.pyplot as plt

def timecourse(sim):
    fig=plt.figure(figsize=(8, 8))
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['font.size'] = 18
    plt.rcParams['lines.linewidth'] = 4
    plt.rcParams['lines.markersize'] = 16
    plt.subplots_adjust(wspace=0.25, hspace=0.3)

    plt.subplot(2, 2, 1)
    plt.plot(sim.t, sim.pAKT[:, 0], 'darkblue')
    plt.plot(sim.t, sim.pAKT[:, 1], 'cornflowerblue')
    plt.plot(sim.t, sim.pAKT[:, 2], 'yellowgreen')
    plt.plot(sim.t, sim.pAKT[:, 3], 'goldenrod')
    plt.plot(sim.t, sim.pAKT[:, 4], 'brown')
    plt.xlim(0, 480)
    plt.xticks([0, 120, 240, 360, 480])
    plt.ylim(0, 1)
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    plt.ylabel('Intensity (A.U.)')
    plt.title('pAKT')

    plt.subplot(2, 2, 2)
    plt.plot(sim.t, sim.pGSK3B[:, 0], 'darkblue')
    plt.plot(sim.t, sim.pGSK3B[:, 1], 'cornflowerblue')
    plt.plot(sim.t, sim.pGSK3B[:, 2], 'yellowgreen')
    plt.plot(sim.t, sim.pGSK3B[:, 3], 'goldenrod')
    plt.plot(sim.t, sim.pGSK3B[:, 4], 'brown')
    plt.xlim(0, 480)
    plt.xticks([0, 120, 240, 360, 480])
    plt.ylim(0, 1)
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    plt.title('pGSK3β')
    
    plt.subplot(2, 2, 3)
    plt.plot(sim.t, sim.pS6K[:, 0], 'darkblue')
    plt.plot(sim.t, sim.pS6K[:, 1], 'cornflowerblue')
    plt.plot(sim.t, sim.pS6K[:, 2], 'yellowgreen')
    plt.plot(sim.t, sim.pS6K[:, 3], 'goldenrod')
    plt.plot(sim.t, sim.pS6K[:, 4], 'brown')
    plt.xlim(0, 480)
    plt.xticks([0, 120, 240, 360, 480])
    #plt.ylim(0, 1)
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    plt.xlabel('                           time (min)')
    plt.ylabel('Intensity (A.U.)')
    plt.title('pS6K')
    
    plt.subplot(2, 2, 4)
    plt.plot(sim.t, sim.G6Pase[:, 0], 'darkblue')
    plt.plot(sim.t, sim.G6Pase[:, 1], 'cornflowerblue')
    plt.plot(sim.t, sim.G6Pase[:, 2], 'yellowgreen')
    plt.plot(sim.t, sim.G6Pase[:, 3], 'goldenrod')
    plt.plot(sim.t, sim.G6Pase[:, 4], 'brown')
    plt.xlim(0, 480)
    plt.xticks([0, 120, 240, 360, 480])
    plt.ylim(0, 1.2)
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])
    plt.xlabel('                           time (min)')
    plt.title('G6Pase')

    

    plt.savefig('Insulin_induced_AKT_pathway.png',bbox_inches='tight')
