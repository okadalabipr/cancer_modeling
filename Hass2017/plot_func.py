from matplotlib import pyplot as plt
import numpy as np

def timecourse(sim):
    """Model trajectories for cell line H322M after EGF stimulation.
    """
    graph_color = ['k','b','c','r','y']
    graph_labelname = ['control, 0 nM', '0.156 nM', '0.625 nM', '2.5 nM', '10.0 nM']
    yticks = [np.arange(0.5,3,0.5), np.arange(-0.8,1.2,0.2), np.arange(-0.8,1,0.2),
                np.arange(-1.2,0,0.2), np.arange(-0.8,0.2,0.2), np.arange(-0.5,0.3,0.1),]
    sd = 1.0E-1
    
    plt.rcParams['font.size'] = 6
    plt.rcParams['font.family'] = 'Arial'
    #plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['lines.linewidth'] = 0.8
    
    plt.subplots_adjust(wspace=0.5, hspace=0.4)
    
    for i in range(6):
        if i<3:
            plt.subplot(2,4,i+1)
        else:
            plt.subplot(2,4,i+2)
        plt.figsize=(7,4)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)

        if i==0:
            for j in range(5):
                plt.plot(sim.t,sim.pEGFR_au[:,j],graph_color[j],label=graph_labelname[j])
                plt.fill_between(sim.t,sim.pEGFR_au[:,j]-sd,sim.pEGFR_au[:,j]+sd,facecolor=graph_color[j],lw=0,alpha=0.1)
            plt.title('pEGFR',fontweight="bold")
            plt.xlabel('time [min]')
            plt.xticks([0,60,120,180,240])
            plt.ylabel('(conc.) [au]')
            plt.yticks(np.arange(0.5,3,0.5))
            plt.ylim([0.4,2.6])
        elif i==1:
            for j in range(5):
                plt.plot(sim.t,sim.pErbB2_au[:,j],graph_color[j],label=graph_labelname[j])
                plt.fill_between(sim.t,sim.pErbB2_au[:,j]-sd,sim.pErbB2_au[:,j]+sd,facecolor=graph_color[j],lw=0,alpha=0.1)
            plt.title('pHER2',fontweight="bold")
            plt.xlabel('time [min]')
            plt.xticks([0,60,120,180,240])
            plt.ylabel('(conc.) [au]')
            plt.yticks(np.arange(-0.8,1.2,0.2))
            plt.ylim([-0.9,1.1])
        elif i==2:
            for j in range(5):
                plt.plot(sim.t,sim.pErbB3_au[:,j],graph_color[j],label=graph_labelname[j])
                plt.fill_between(sim.t,sim.pErbB3_au[:,j]-sd,sim.pErbB3_au[:,j]+sd,facecolor=graph_color[j],lw=0,alpha=0.1)
            plt.title('pErbB3',fontweight="bold")
            plt.xlabel('time [min]')
            plt.xticks([0,60,120,180,240])
            plt.ylabel('(conc.) [au]')
            plt.yticks(np.arange(-0.8,1,0.2))
            plt.ylim([-0.9,0.9])

            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, frameon=False)
        elif i==3:
            for j in range(5):
                plt.plot(sim.t,sim.pERK_au[:,j],graph_color[j],label=graph_labelname[j])
                plt.fill_between(sim.t,sim.pERK_au[:,j]-sd,sim.pERK_au[:,j]+sd,facecolor=graph_color[j],lw=0,alpha=0.1)
            plt.title('pERK',fontweight="bold")
            plt.xlabel('time [min]')
            plt.xticks([0,60,120,180,240])
            plt.ylabel('(conc.) [au]')
            plt.yticks(np.arange(-1.2,0,0.2))
            plt.ylim([-1.2,0])
        elif i==4:
            for j in range(5):
                plt.plot(sim.t,sim.pAKT_au[:,j],graph_color[j],label=graph_labelname[j])
                plt.fill_between(sim.t,sim.pAKT_au[:,j]-sd,sim.pAKT_au[:,j]+sd,facecolor=graph_color[j],lw=0,alpha=0.1)
            plt.title('pAKT',fontweight="bold")
            plt.xlabel('time [min]')
            plt.xticks([0,60,120,180,240])
            plt.ylabel('(conc.) [au]')
            plt.yticks(np.arange(-0.8,0.2,0.2))
            plt.ylim([-1,0.2])
        elif i==5:
            for j in range(5):
                plt.plot(sim.t,sim.pS6_au[:,j],graph_color[j],label=graph_labelname[j])
                plt.fill_between(sim.t,sim.pS6_au[:,j]-sd,sim.pS6_au[:,j]+sd,facecolor=graph_color[j],lw=0,alpha=0.1)
            plt.title('pS6',fontweight="bold")
            plt.xlabel('time [min]')
            plt.xticks([0,60,120,180,240])
            plt.ylabel('(conc.) [au]')
            plt.yticks(np.arange(-0.5,0.3,0.1))
            plt.ylim([-0.6,0.2])
            
    plt.savefig('H322M_EGF.png',dpi=300,bbox_inches='tight')