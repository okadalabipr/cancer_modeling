from matplotlib import pyplot as plt

def timecourse(sim):
    plt.figure(figsize=(16,13))
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 15
    plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['lines.linewidth'] = 1.5

    plt.subplots_adjust(wspace=0.4, hspace=0.5)
    
    plt.subplot(3,4,1)
    plt.plot(sim.t,1*(sim.t>1),'k')
    plt.xlim(0,7)
    plt.xticks([0,2,4,6])
    plt.ylim(0,1.5)
    plt.title('TNF activity')
    
    plt.subplot(3,4,2)
    plt.plot(sim.t,sim.Neutral_IKK,'k',clip_on=False)
    plt.xlim(0,7)
    plt.xticks([0,2,4,6])
    plt.ylim(0,0.2)
    plt.title('Neutral IKK (IKKn)')
    
    plt.subplot(3,4,3)
    plt.plot(sim.t,sim.Active_IKK,'k')
    plt.xlim(0,7)
    plt.xticks([0,2,4,6])
    plt.ylim(0,0.1)
    plt.title('Active IKK (IKKa)')

    plt.subplot(3,4,4)
    plt.plot(sim.t,sim.Inactive_IKK,'k')
    plt.xlim(0,7)
    plt.xticks([0,2,4,6])
    plt.ylim(0,0.2)
    plt.title('Inactive IKK (IKKi)')
    
    plt.subplot(3,4,5)
    plt.plot(sim.t,sim.Free_cyt_IkBa,'k')
    plt.xlim(0,7)
    plt.xticks([0,2,4,6])
    plt.ylim(0,0.04)
    plt.title('Free cyt. IkBa')
    
    plt.subplot(3,4,6)
    plt.plot(sim.t,sim.Cyt,'k')
    plt.xlim(0,7)
    plt.xticks([0,2,4,6])
    plt.ylim(0,0.06)
    plt.title('Cyt. (IkBa|NFkB)')
    
    plt.subplot(3,4,7)
    plt.plot(sim.t,sim.Free_nuclear_IkBa,'k')
    plt.xlim(0,7)
    plt.xticks([0,2,4,6])
    plt.ylim(0,0.02)
    plt.title('Free nuclear IkBa')
    
    plt.subplot(3,4,8)
    plt.plot(sim.t,sim.Free_nuclear_NFkB,'k')
    plt.xlim(0,7)
    plt.xticks([0,2,4,6])
    plt.ylim(0,0.4)
    plt.title('Free nuclear NFkB')
    
    plt.subplot(3,4,9)
    plt.plot(sim.t,sim.IkBa_mRNA*1e4,'k')
    plt.xlim(0,7)
    plt.xticks([0,2,4,6])
    plt.title(r'× 10$^4$ IkBa mRNA')
    
    plt.subplot(3,4,10)
    plt.plot(sim.t,sim.A20_mRNA*1e4,'k')
    plt.xlim(0,7)
    plt.xticks([0,2,4,6])
    plt.title(r'× 10$^4$ A20 mRNA')

    plt.subplot(3,4,11)
    plt.plot(sim.t,sim.A20_protein,'k')
    plt.xlim(0,7)
    plt.xticks([0,2,4,6])
    plt.ylim(0,0.2)
    plt.title('A20 protein')
    
    plt.subplot(3,4,12)
    plt.plot(sim.t,sim.cgen_mRNA*1e4,'k')
    plt.xlim(0,7)
    plt.xticks([0,2,4,6])
    plt.title(r'× 10$^4$ cgen mRNA')
    
    plt.show()