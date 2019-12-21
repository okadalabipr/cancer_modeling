import matplotlib.pyplot as plt

from model.name2idx import variables as V

def timecourse(sim):
    plt.rcParams['font.size'] = 16
    fig, ax1 = plt.subplots(figsize=(6,4))
    ax2 = ax1.twinx()


    ax1.plot(sim.t,sim.Y[:,V.MC],'c')
    ax1.plot(sim.t,sim.Y[:,V.MP],'m')
    ax1.set_xlim([0,72])
    ax1.set_xticks([0,12,24,36,48,60,72])
    ax1.set_xlabel('Time (h)')
    ax1.set_ylim([0,5])
    ax1.set_ylabel(r'$\it{Per}$'+' '+r'$\sf{(M_P)}$'+' and '+
        r'$\it{Cry}$'+' '+r'$\sf{(M_C)}$'+'\nmRNAs, nM')

    ax2.plot(sim.t,sim.Y[:,V.MB],'y')
    ax2.set_ylim([7,10])
    ax2.set_yticks([7,8,9,10])
    ax2.set_ylabel(r'$\it{Bmal1}$'+' mRNA '+r'$\sf{(M_B)}$'+', nM')

    plt.savefig('Per_Cry_Bmal1mRNA.png',bbox_inches='tight')