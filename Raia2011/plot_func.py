from matplotlib import pyplot as plt

def timecourse(sim):
    plt.figure(figsize=(20,15))
    
    plt.rcParams['font.size'] = 24
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['lines.linewidth'] = 2
    
    plt.subplots_adjust(wspace=0.5, hspace=0.6)
    
    plt.subplot(4,4,1)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.IL13stimulation[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.IL13stimulation[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.IL13stimulation[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.IL13stimulation[:,3],'b',label='0.0ng/mL')
    plt.title('IL13stimulation')
    plt.ylabel('IL13 (ng/mL)')
    plt.xticks([0,50,100])
    plt.yticks([0,20,40,60,80])
    
    
    plt.subplot(4,4,2)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.Rec[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.Rec[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.Rec[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.Rec[:,3],'b',label='0.0ng/mL')
    plt.title('Rec')
    plt.ylabel('Molecules/cell(×1,000)')
    plt.xticks([0,50,100])
    plt.yticks([0,0.5,1,1.5])
    
    
    plt.subplot(4,4,3)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.Rec_i[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.Rec_i[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.Rec_i[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.Rec_i[:,3],'b',label='0.0ng/mL')
    plt.title('Rec_i')
    plt.xticks([0,50,100])
    plt.yticks([100,105,110])
    

    
    plt.subplot(4,4,4)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.IL13_Rec[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.IL13_Rec[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.IL13_Rec[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.IL13_Rec[:,3],'b',label='0.0ng/mL')
    plt.title('IL13_Rec')
    plt.xticks([0,50,100])
    plt.yticks([0,0.01,0.02])
    

    
    plt.subplot(4,4,5)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.p_IL13_Rec[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.p_IL13_Rec[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.p_IL13_Rec[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.p_IL13_Rec[:,3],'b',label='0.0ng/mL')
    plt.title('p_IL13_Rec')
    plt.ylabel('Molecules/cell\n(×1,000)')
    plt.xticks([0,50,100])
    plt.yticks([0,0.5,1])
    
    
    plt.subplot(4,4,6)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.p_IL13_Rec_i[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.p_IL13_Rec_i[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.p_IL13_Rec_i[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.p_IL13_Rec_i[:,3],'b',label='0.0ng/mL')
    plt.title('p_IL13_Rec_i')
    plt.xticks([0,50,100])
    plt.yticks([0,0.5])
    
    
    plt.subplot(4,4,7)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.JAK2[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.JAK2[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.JAK2[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.JAK2[:,3],'b',label='0.0ng/mL')
    plt.title('JAK2')
    plt.xticks([0,50,100])
    plt.yticks([1,2,3])
    
    
    
    plt.subplot(4,4,8)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.pJAK2[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.pJAK2[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.pJAK2[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.pJAK2[:,3],'b',label='0.0ng/mL')
    plt.title('pJAK2')
    plt.xticks([0,50,100])
    plt.yticks([0,1,2])
    
    
    plt.subplot(4,4,9)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.SHP1[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.SHP1[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.SHP1[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.SHP1[:,3],'b',label='0.0ng/mL')
    plt.title('SHP1')
    plt.ylabel('Molecules/cell\n(×1,000)')
    plt.ylim([90,92])
    plt.xticks([0,50,100])
    plt.yticks([90,91,92])
    
    
    plt.subplot(4,4,10)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.STAT5[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.STAT5[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.STAT5[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.STAT5[:,3],'b',label='0.0ng/mL')
    plt.title('STAT5')
    plt.xticks([0,50,100])
    plt.yticks([50,100,150])
    
    
    plt.subplot(4,4,11)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.pSTAT5[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.pSTAT5[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.pSTAT5[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.pSTAT5[:,3],'b',label='0.0ng/mL')
    plt.title('pSTAT5')
    plt.xticks([0,50,100])
    plt.yticks([0,50,100])
    
    
    plt.subplot(4,4,12)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.SOCS3mRNA[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.SOCS3mRNA[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.SOCS3mRNA[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.SOCS3mRNA[:,3],'b',label='0.0ng/mL')
    plt.title('SOCS3mRNA')
    
    
    plt.subplot(4,4,13)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.DecoyR[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.DecoyR[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.DecoyR[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.DecoyR[:,3],'b',label='0.0ng/mL')
    plt.title('DecoyR')
    plt.ylabel('Molecules/cell\n(×1,000)')
    plt.xlabel('Time (min)')
    plt.xticks([0,50,100])
    plt.yticks([0,2])
    
        
    plt.subplot(4,4,14)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.IL13_DecoyR[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.IL13_DecoyR[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.IL13_DecoyR[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.IL13_DecoyR[:,3],'b',label='0.0ng/mL')
    plt.title('IL13_DecoyR')
    plt.xlabel('Time (min)')
    plt.xticks([0,50,100])
    plt.yticks([0,2])
    
        
    plt.subplot(4,4,15)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.SOCS3[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.SOCS3[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.SOCS3[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.SOCS3[:,3],'b',label='0.0ng/mL')
    plt.title('SOCS3')
    plt.xlabel('Time (min)')
    plt.xticks([0,50,100])
    plt.yticks([0,100,200])

    
    plt.subplot(4,4,16)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.plot(sim.t,sim.CD274mRNA[:,0],'r',label='80.0ng/mL')
    plt.plot(sim.t,sim.CD274mRNA[:,1],'y',label='20.0ng/mL')
    plt.plot(sim.t,sim.CD274mRNA[:,2],'g',label='4.0ng/mL')
    plt.plot(sim.t,sim.CD274mRNA[:,3],'b',label='0.0ng/mL')
    plt.title('CD274mRNA')
    plt.xlabel('Time (min)')
    
    plt.savefig('MedB1model.png',bbox_inches='tight')