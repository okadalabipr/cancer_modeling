from matplotlib import pyplot as plt
import numpy as np

from model.name2idx import parameters as C
from model.param_const import f_params

def timecourse(sim):

    x = f_params()

    yticks = [np.arange(-0.4,0.6,0.2)]
    
    plt.rcParams['font.size'] = 6
    plt.rcParams['font.family'] = 'Arial'
    #plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['lines.linewidth'] = 2
    plt.subplots_adjust(wspace=0.3, hspace=1.0)
    
    for i in range(12):
        plt.subplot(4,3,i+1)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        if i==0:
            plt.plot(sim.t,sim.Ski_treated,'r')
            plt.fill_between(sim.t,sim.Ski_treated-x[C.sd_Ski],sim.Ski_treated+x[C.sd_Ski],facecolor='r',lw=0,alpha=0.1)
            plt.title('Ski (Cluster 1)',fontweight="bold")
            plt.ylim([-0.5,0.7])
            plt.yticks([-0.4,-0.2,0,0.2,0.4,0.6])
        elif i==1:
            plt.plot(sim.t,sim.Skil_treated,'r')
            plt.fill_between(sim.t,sim.Skil_treated-x[C.sd_Skil],sim.Skil_treated+x[C.sd_Skil],facecolor='r',lw=0,alpha=0.1)
            plt.title('Skil (Cluster 2)',fontweight="bold")
            plt.ylim([-0.2,1.2])
            plt.yticks([0,0.5,1.0])
        elif i==2:
            plt.plot(sim.t,sim.Dnmt3a_treated,'r')
            plt.fill_between(sim.t,sim.Dnmt3a_treated-x[C.sd_Dnmt3a],sim.Dnmt3a_treated+x[C.sd_Dnmt3a],facecolor='r',lw=0,alpha=0.1)
            plt.title('Dnmt3a (Cluster 3)',fontweight="bold")
            plt.ylim([-0.2,0.5])
            plt.yticks([-0.2,0,0.2,0.4])
        elif i==3:
            plt.plot(sim.t,sim.Sox4_treated,'r')
            plt.fill_between(sim.t,sim.Sox4_treated-x[C.sd_Sox4],sim.Sox4_treated+x[C.sd_Sox4],facecolor='r',lw=0,alpha=0.1)
            plt.title('Sox4 (Cluster 4)',fontweight="bold")
            plt.ylim([-0.6,1.0])
            plt.yticks([-0.5,0.0,0.5])
        elif i==4:
            plt.plot(sim.t,sim.Jun_treated,'r')
            plt.fill_between(sim.t,sim.Jun_treated-x[C.sd_Jun],sim.Jun_treated+x[C.sd_Jun],facecolor='r',lw=0,alpha=0.1)
            plt.title('Jun (Cluster 5)',fontweight="bold")
            plt.ylim([-0.8,1.0])
            plt.yticks([-0.5,0,0.5,1.0])
        elif i==5:
            plt.plot(sim.t,sim.Smad7_treated,'r')
            plt.fill_between(sim.t,sim.Smad7_treated-x[C.sd_Smad7],sim.Smad7_treated+x[C.sd_Smad7],facecolor='r',lw=0,alpha=0.1)
            plt.title('Smad7 (Cluster 6)',fontweight="bold")
            plt.ylim([-0.5,1.1])
            plt.yticks([0,0.5,1.0])
        elif i==6:
            plt.plot(sim.t,sim.Klf10_treated,'r')
            plt.fill_between(sim.t,sim.Klf10_treated-x[C.sd_Klf10],sim.Klf10_treated+x[C.sd_Klf10],facecolor='r',lw=0,alpha=0.1)
            plt.title('Klf10 (Cluster 7)',fontweight="bold")
            plt.ylim([-0.3,1.5])
            plt.yticks([0,0.5,1.0,1.5])
        elif i==7:
            plt.plot(sim.t,sim.Bmp4_treated,'r')
            plt.fill_between(sim.t,sim.Bmp4_treated-x[C.sd_Bmp4],sim.Bmp4_treated+x[C.sd_Bmp4],facecolor='r',lw=0,alpha=0.1)
            plt.title('Bmp4 (Cluster 8)',fontweight="bold")
            plt.ylim([-0.5,0.6])
            plt.yticks([-0.4,-0.2,0,0.2,0.4])
        elif i==8:
            plt.plot(sim.t,sim.Cxcl15_treated,'r')
            plt.fill_between(sim.t,sim.Cxcl15_treated-x[C.sd_Cxcl15],sim.Cxcl15_treated+x[C.sd_Cxcl15],facecolor='r',lw=0,alpha=0.1)
            plt.title('Cxcl15 (Cluster 9)',fontweight="bold")
            plt.ylim([-0.5,0.4])
            plt.yticks([-0.4,-0.2,0,0.2])
        elif i==9:
            plt.plot(sim.t,sim.Dusp5_treated,'r')
            plt.fill_between(sim.t,sim.Dusp5_treated-x[C.sd_Dusp5],sim.Dusp5_treated+x[C.sd_Dusp5],facecolor='r',lw=0,alpha=0.1)
            plt.title('Dusp5 (Cluster 10)',fontweight="bold")
            plt.ylim([-0.4,0.3])
            plt.yticks([-0.2,0,0.2])
        elif i==10:
            plt.plot(sim.t,sim.Tgfa_treated,'r')
            plt.fill_between(sim.t,sim.Tgfa_treated-x[C.sd_Tgfa],sim.Tgfa_treated+x[C.sd_Tgfa],facecolor='r',lw=0,alpha=0.1)
            plt.title('Tgfa (Cluster 11)',fontweight="bold")
            plt.ylim([-0.6,0.2])
            plt.yticks([-0.4,-0.2,0,0.2])
        elif i==11:
            plt.plot(sim.t,sim.Pdk4_treated,'r')
            plt.fill_between(sim.t,sim.Pdk4_treated-x[C.sd_Pdk4],sim.Pdk4_treated+x[C.sd_Pdk4],facecolor='r',lw=0,alpha=0.1)
            plt.title('Pdk4 (Cluster 12)',fontweight="bold")
            plt.ylim([-0.6,0.1])
            plt.yticks([-0.4,-0.2,0])
        
        if i>=9:
            plt.xlabel('time (min)')
        plt.xticks([0,120,240,360,480,600])
        if i%3==0:
            plt.ylabel('gene expression(log2)')

    plt.show()