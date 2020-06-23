import matplotlib.pyplot as plt

from model.name2idx import V

def timecourse(sim):
    plt.figure(figsize=(9,6))
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 16
    plt.rcParams['axes.linewidth'] = 1.5
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.markersize'] = 20

    plt.plot(sim.t,sim.p27_tot,'r-')
    plt.plot(sim.t,sim.Y[:,V.CycET],'b-')
    plt.plot(sim.t,sim.CyclinE,'b--')
    plt.plot(sim.t,sim.Y[:,V.CycAT],'g-')
    plt.plot(sim.t,sim.CyclinA,'g--')

    plt.xticks([0,300,600,900],[-5,0,5,10])
    plt.xlim([0,900])
    plt.xlabel('time relative to G1/S transition(h)')
    plt.yticks([0,0.3,0.6,0.9])
    plt.ylabel('relative levels')

    plt.text(3.2*60,0.75,'p27',ha='center',va='bottom',color='r')
    plt.text(6.4*60,0.82,'CycE level',ha='center',va='bottom',color='b')
    plt.text(6.4*60,0.55,'free\nCycE:Cdk2',ha='center',va='bottom',color='b')
    plt.text(12.4*60,0.6,'CycA level',ha='center',va='bottom',color='g')
    plt.text(12.4*60,0.35,'free\nCycA:Cdk2',ha='center',va='bottom',color='g')

    plt.savefig('./p27_CycE_CycAlevel.png',bbox_inches='tight')