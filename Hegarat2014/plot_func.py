from matplotlib import pyplot as plt

def timecourse(sim):
    
    plt.figure(figsize=(20,15))
    plt.rcParams['font.size'] = 20
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['lines.linewidth'] = 2
    plt.subplots_adjust(wspace=0.3, hspace=0.4)
    
    for i in range(9):
        plt.subplot(3,3,i+1)
        plt.plot(sim.t,sim.Gwl[:,i],'mediumblue',label='Gwl')
        plt.plot(sim.t,sim.Cdc25[:,i],'lime',label='Cdc25')
        plt.plot(sim.t,sim.ENSAP[:,i],'orange',label='ENSAP')
        if i in [3,4,5]: 
            plt.xticks([0,20,40,60,80,100,120])
            plt.xlim(0,120)
        else:
            plt.plot(sim.t,sim.B55[:,i],'darkviolet',label='B55')
            plt.xticks([0,5,10,15,20,25,30])
            plt.xlim(0,30)
        plt.plot(sim.t,sim.Y15[:,i],'r',label='Y15')
        
        plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])
        plt.ylim(0,1.05)
        plt.xlabel('Time (min)')
        
        if i==0:
            plt.title('OA insensitive phosphatase')
            plt.ylabel('Cdk1 Inhibition and \nrelease')
        if i==1:
            plt.title('OA sensitive phosphatase')
        if i==2:
            plt.title('PP2A-B55')
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
        if i==3:
            plt.ylabel('Cdk1 Inhibition +OA')
        if i==6:
            plt.ylabel('Cdk1 Inhibition')
    
    plt.savefig('mitotic_switch.png',bbox_inches='tight')