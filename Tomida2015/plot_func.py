import numpy as np
import matplotlib.pyplot as plt

def timecourse(sim):
    fig=plt.figure(figsize=(4,12))
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 15
    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['lines.linewidth'] = 2

    plt.subplots_adjust(wspace=0.5, hspace=0.3)

    for i in range(sim.condition):
        plt.subplot(4,1,i+1)

        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().yaxis.set_ticks_position('left')
        plt.gca().xaxis.set_ticks_position('bottom')

        plt.plot(sim.t,np.zeros(len(sim.t)),'--',color='darkgray')
        plt.plot(sim.t,sim.p38_activity[:,i],label='p38 reporter')

        plt.xlim([-20,480])
        plt.xticks([60*i for i in range(9)])
        plt.ylim([-0.05,0.6])
        plt.yticks([0.1*i for i in range(7)])
        if i==0:
                plt.legend(loc='upper right',frameon=False)
        fig.text(0.5, 0.08, 'Time (min)', ha='center')
        fig.text(-0.05, 0.5, 'p38 activity (a.u.)', va='center', rotation='vertical')

    fig.text(0.5, 0.82, r'$k_8$ = 0.024', ha='center')
    fig.text(0.5, 0.62, r'$k_8$ = 0.012', ha='center')
    fig.text(0.5, 0.42, r'$k_8$ = 0.008', ha='center')
    fig.text(0.5, 0.22, r'$k_8$ = 0.004', ha='center')

    plt.savefig('p38_activity.png',bbox_inches='tight')