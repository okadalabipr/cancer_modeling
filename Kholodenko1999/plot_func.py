import matplotlib.pyplot as plt

def timecourse(sim):
    fig=plt.figure(figsize=(9,9))
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['lines.linewidth'] = 2

    plt.subplots_adjust(wspace=0.5, hspace=0.4)

    plt.subplot(2,2,1)
    plt.plot(sim.t,sim.totalShc[:,0],'g')
    plt.plot(sim.t,sim.totalShc[:,1],'g',alpha=0.5)
    plt.plot(sim.t,sim.totalGrb2[:,0],'m')
    plt.plot(sim.t,sim.totalGrb2[:,1],'m',alpha=0.5)
    plt.xlim(0,120)
    plt.xticks([30*i for i in range(5)])
    plt.ylim(0,150)
    plt.xlabel("TIME (s)")
    plt.ylabel("Protein concentrations (nM)")

    plt.subplot(2,2,2)
    plt.plot(sim.t,sim.RSh[:,0],'g')
    plt.plot(sim.t,sim.RSh[:,1],'g',alpha=0.5)
    plt.plot(sim.t,sim.RGrb2[:,0],'m')
    plt.plot(sim.t,sim.RGrb2[:,1],'m',alpha=0.5)
    plt.xlim(0,120)
    plt.xticks([30*i for i in range(5)])
    plt.ylim(0,25)
    plt.xlabel("TIME (s)")
    plt.ylabel("Protein concentrations (nM)")

    ax1=plt.subplot(2,2,3)
    ax2 = ax1.twinx()
    ax1.plot(sim.t,sim.totalSOS[:,0],'g')
    ax1.plot(sim.t,sim.totalSOS[:,1],'g',alpha=0.5)
    ax2.plot(sim.t,sim.ShGS[:,0],'m')
    ax2.plot(sim.t,sim.ShGS[:,1],'m',alpha=0.5)
    ax1.set_xlim(0,120)
    ax1.set_xticks([30*i for i in range(5)])
    ax1.set_xlabel("TIME (s)")
    ax1.set_ylim(0,8)
    ax2.set_ylim(0,30)
    ax1.set_ylabel("SOS bound to EGFR (nM)")
    ax2.set_ylabel("Concentration of Sh-G-S (nM)")

    ax1=plt.subplot(2,2,4)
    ax2 = ax1.twinx()
    ax1.plot(sim.t,sim.PLCg[:,0],'g')
    ax1.plot(sim.t,sim.PLCg[:,1],'g',alpha=0.5)
    ax2.plot(sim.t,sim.PLCg[:,2],'g--')
    ax1.set_xlim(0,120)
    ax1.set_xticks([30*i for i in range(5)])
    ax1.set_ylim(0,15)
    ax1.set_xlabel("TIME (s)")
    ax1.set_ylabel("Total Phosphorylated PLCγ (nM)")
    ax2.set_ylim(0,105)
    ax2.set_yticks([30*i for i in range(4)])

    #plt.show()
    plt.savefig('EGFsignaling.png',bbox_inches='tight')