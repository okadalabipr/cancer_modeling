import matplotlib.pyplot as plt

def timecourse(sim):
    fig=plt.figure(figsize=(9,9))
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 18
    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['lines.linewidth'] = 3
    plt.rcParams['lines.markersize'] = 16
    plt.subplots_adjust(wspace=0, hspace=0.3)

    plt.subplot(2,1,1)
    plt.title('nuclear IκBα')
    plt.plot(sim.t,sim.nuclear_IkBa[:,0],'k',label='TNFα')
    plt.plot(sim.t,sim.nuclear_IkBa[:,1],'r',label='TNFα + DCF')
    plt.xticks([0,50,100,150,200])
    plt.yticks([0,0.05,0.10,0.15])
    plt.legend(loc='upper left',frameon=False)

    plt.subplot(2,1,2)
    plt.plot(sim.t,sim.nuclear_NFKB[:,0],'k',label='TNFα')
    plt.plot(sim.t,sim.nuclear_NFKB[:,1],'r',label='TNFα + DCF')
    plt.title('nuclear NFκB')
    #plt.xlabel('time [min]')
    plt.xticks([0,50,100,150,200])

    fig.text(0.5, 0.05, 'time [min]', ha='center')
    fig.text(0.0, 0.5, 'concentration [a.u.]', va='center', rotation='vertical')

    plt.show()