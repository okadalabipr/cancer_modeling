from matplotlib import pyplot as plt

def timecourse(sim):
    plt.figure(figsize=(9,6))
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['mathtext.fontset'] = 'custom'
    plt.rcParams['mathtext.it'] = 'Arial:italic'
    plt.rcParams['font.size'] = 16
    plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['lines.linewidth'] = 3
    
    plt.plot(sim.t,sim.totalNumPSmad2_sustained,'b',label=r'Sustained TGF-$\beta$ stimulation')
    plt.plot(sim.t,sim.totalNumPSmad2_singlePulse,'r',label='Single pulse of 30 s\n'+r'TGF-$\beta$ stimulation')

    plt.ylabel('P-Smad2 (molecules/cell)')
    plt.xlabel('Time (h)')
    plt.yticks([0,10000,20000,30000])
    plt.ylim(-3000,35000)
    plt.legend(loc='best',frameon=False)
    
    plt.show()