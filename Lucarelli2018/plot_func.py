from matplotlib import pyplot as plt
import numpy as np

from model.name2idx import parameters as C
from model.param_const import f_params

def timecourse(sim):

    x = f_params()

    yticks = [np.arange(-0.4,0.6,0.2)]
    
    plt.rcParams['font.size'] = 6
    #plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['lines.linewidth'] = 2
    plt.subplots_adjust(wspace=0.2, hspace=1.0)
    
    for i in range(12):
        plt.subplot(4,3,i+1)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        if i==0:
            plt.plot(sim.t,sim.Ski,'k',linewidth = 1.5)
            plt.plot(sim.t,sim.Ski_red,color='brown',linewidth = 1.5)
            plt.plot(sim.t,sim.Ski_blue,color='steelblue',linewidth = 1.5)
            plt.plot(sim.t,sim.Ski_green,'g',linewidth = 1.5)
            plt.title('Ski',fontweight="bold")
            plt.yticks([0,1,2])
        elif i==1:
            plt.plot(sim.t,sim.Skil,'k',linewidth = 1.5)
            plt.plot(sim.t,sim.Skil_red,color='brown',linewidth = 1.5)
            plt.plot(sim.t,sim.Skil_blue,color='steelblue',linewidth = 1.5)
            plt.plot(sim.t,sim.Skil_green,'g',linewidth = 1.5)
            plt.title('Skil',fontweight="bold")
            plt.yticks([0,1,2,3])
        elif i==2:
            plt.plot(sim.t,sim.Dnmt3a,'k',linewidth = 1.5)
            plt.plot(sim.t,sim.Dnmt3a_red,color='brown',linewidth = 1.5)
            plt.plot(sim.t,sim.Dnmt3a_blue,color='steelblue',linewidth = 1.5)
            plt.plot(sim.t,sim.Dnmt3a_green,'g',linewidth = 1.5)
            plt.title('Dnmt3a',fontweight="bold")
            plt.yticks([0,0.5,1,1.5])
        elif i==3:
            plt.plot(sim.t,sim.Sox4,'k',linewidth = 1.5)
            plt.plot(sim.t,sim.Sox4_red,color='brown',linewidth = 1.5)
            plt.plot(sim.t,sim.Sox4_blue,color='steelblue',linewidth = 1.5)
            plt.plot(sim.t,sim.Sox4_green,'g',linewidth = 1.5)
            plt.title('Sox4',fontweight="bold")
            plt.yticks([0,1,2])
        elif i==4:
            plt.plot(sim.t,sim.Jun,'k',linewidth = 1.5)
            plt.plot(sim.t,sim.Jun_red,color='brown',linewidth = 1.5)
            plt.plot(sim.t,sim.Jun_blue,color='steelblue',linewidth = 1.5)
            plt.plot(sim.t,sim.Jun_green,'g',linewidth = 1.5)
            plt.title('Jun',fontweight="bold")
            plt.yticks([0,1,2,3])
        elif i==5:
            plt.plot(sim.t,sim.Smad7,'k',linewidth = 1.5)
            plt.plot(sim.t,sim.Smad7_red,color='brown',linewidth = 1.5)
            plt.plot(sim.t,sim.Smad7_blue,color='steelblue',linewidth = 1.5)
            plt.plot(sim.t,sim.Smad7_green,'g',linewidth = 1.5)
            plt.title('Smad7',fontweight="bold")
            plt.yticks([0,1,2,3])
        elif i==6:
            plt.plot(sim.t,sim.Klf10,'k',linewidth = 1.5)
            plt.plot(sim.t,sim.Klf10_red,color='brown',linewidth = 1.5)
            plt.plot(sim.t,sim.Klf10_blue,color='steelblue',linewidth = 1.5)
            plt.plot(sim.t,sim.Klf10_green,'g',linewidth = 1.5)
            plt.title('Klf10',fontweight="bold")
            plt.yticks([0,2,4])
        elif i==7:
            plt.plot(sim.t,sim.Bmp4,'k',linewidth = 1.5)
            plt.plot(sim.t,sim.Bmp4_red,color='brown',linewidth = 1.5)
            plt.plot(sim.t,sim.Bmp4_blue,color='steelblue',linewidth = 1.5)
            plt.plot(sim.t,sim.Bmp4_green,'g',linewidth = 1.5)
            plt.title('Bmp4',fontweight="bold")
            plt.yticks([0,1,2])
        elif i==8:
            plt.plot(sim.t,sim.Cxcl15,'k',linewidth = 1.5)
            plt.plot(sim.t,sim.Cxcl15_red,color='brown',linewidth = 1.5)
            plt.plot(sim.t,sim.Cxcl15_blue,color='steelblue',linewidth = 1.5)
            plt.plot(sim.t,sim.Cxcl15_green,'g',linewidth = 1.5)
            plt.title('Cxcl15',fontweight="bold")
            plt.yticks([-1.5,-1,-0.5,0,0.5])
        elif i==9:
            plt.plot(sim.t,sim.Dusp5,'k',linewidth = 1.5)
            plt.plot(sim.t,sim.Dusp5_red,color='brown',linewidth = 1.5)
            plt.plot(sim.t,sim.Dusp5_blue,color='steelblue',linewidth = 1.5)
            plt.plot(sim.t,sim.Dusp5_green,'g',linewidth = 1.5)
            plt.title('Dusp5',fontweight="bold")
            plt.yticks([-1.5,-1,-0.5,0])
        elif i==10:
            plt.plot(sim.t,sim.Tgfa,'k',linewidth = 1.5)
            plt.plot(sim.t,sim.Tgfa_red,color='brown',linewidth = 1.5)
            plt.plot(sim.t,sim.Tgfa_blue,color='steelblue',linewidth = 1.5)
            plt.plot(sim.t,sim.Tgfa_green,'g',linewidth = 1.5)
            plt.title('Tgfa',fontweight="bold")
            plt.yticks([-1.5,-1,-0.5,0,0.5])
        elif i==11:
            plt.plot(sim.t,sim.Pdk4,'k',linewidth = 1.5)
            plt.plot(sim.t,sim.Pdk4_red,color='brown',linewidth = 1.5)
            plt.plot(sim.t,sim.Pdk4_blue,color='steelblue',linewidth = 1.5)
            plt.plot(sim.t,sim.Pdk4_green,'g',linewidth = 1.5)
            plt.title('Pdk4',fontweight="bold")
            plt.yticks([-3,-2,-1,0])
        
        if i>=9:
            plt.xlabel('time (min)')
        plt.xticks([0,200,400,600])
        if i%3==0:
            plt.ylabel('gene expression(log2)',fontweight="bold")

    plt.show()