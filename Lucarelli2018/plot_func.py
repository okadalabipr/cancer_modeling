from matplotlib import pyplot as plt
import numpy as np


def timecourse(sim):

    plt.figure(figsize=(10,10))
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['mathtext.fontset'] = 'custom'
    plt.rcParams['mathtext.it'] = 'Arial:italic'
    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['xtick.major.width'] = 2
    plt.rcParams['ytick.major.width'] = 2
    plt.rcParams['lines.linewidth'] = 2
    plt.subplots_adjust(wspace=0.3, hspace=0.8)

    for i, gene_name in enumerate(sim.conditions):
        plt.subplot(4, 3, i+1)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        if gene_name == 'Ski':
            plt.plot(sim.t, sim.Ski_WT, color='brown', linewidth=1.5)
            plt.plot(sim.t, sim.Ski_Smad2OE, color='royalblue', linewidth=1.5)
            plt.plot(sim.t, sim.Ski_Smad3OE, color='darkgreen', linewidth=1.5)
            plt.plot(sim.t, sim.Ski_Smad4OE, 'k', linewidth=1.5)
            plt.title(r'$\it{Ski}$')
            plt.yticks([0, 1, 2])
        elif gene_name == 'Skil':
            plt.plot(sim.t, sim.Skil_WT, color='brown', linewidth=1.5)
            plt.plot(sim.t, sim.Skil_Smad2OE, color='royalblue', linewidth=1.5)
            plt.plot(sim.t, sim.Skil_Smad3OE, color='darkgreen', linewidth=1.5)
            plt.plot(sim.t, sim.Skil_Smad4OE, 'k', linewidth=1.5)
            plt.title(r'$\it{Skil}$')
            plt.yticks([0, 1, 2, 3])
        elif gene_name == 'Dnmt3a':
            plt.plot(sim.t, sim.Dnmt3a_WT, color='brown', linewidth=1.5)
            plt.plot(sim.t, sim.Dnmt3a_Smad2OE, color='royalblue', linewidth=1.5)
            plt.plot(sim.t, sim.Dnmt3a_Smad3OE, color='darkgreen', linewidth=1.5)
            plt.plot(sim.t, sim.Dnmt3a_Smad4OE, 'k', linewidth=1.5)
            plt.title(r'$\it{Dnmt3a}$')
            plt.yticks([0, 0.5, 1, 1.5])
        elif gene_name == 'Sox4':
            plt.plot(sim.t, sim.Sox4_WT, color='brown', linewidth=1.5)
            plt.plot(sim.t, sim.Sox4_Smad2OE, color='royalblue', linewidth=1.5)
            plt.plot(sim.t, sim.Sox4_Smad3OE, color='darkgreen', linewidth=1.5)
            plt.plot(sim.t, sim.Sox4_Smad4OE, 'k', linewidth=1.5)
            plt.title(r'$\it{Sox4}$')
            plt.yticks([0, 1, 2])
        elif gene_name == 'Jun':
            plt.plot(sim.t, sim.Jun_WT, color='brown', linewidth=1.5)
            plt.plot(sim.t, sim.Jun_Smad2OE, color='royalblue', linewidth=1.5)
            plt.plot(sim.t, sim.Jun_Smad3OE, color='darkgreen', linewidth=1.5)
            plt.plot(sim.t, sim.Jun_Smad4OE, 'k', linewidth=1.5)
            plt.title(r'$\it{Jun}$')
            plt.yticks([0, 1, 2, 3])
        elif gene_name == 'Smad7':
            plt.plot(sim.t, sim.Smad7_WT, color='brown', linewidth=1.5)
            plt.plot(sim.t, sim.Smad7_Smad2OE, color='royalblue', linewidth=1.5)
            plt.plot(sim.t, sim.Smad7_Smad3OE, color='darkgreen', linewidth=1.5)
            plt.plot(sim.t, sim.Smad7_Smad4OE, 'k', linewidth=1.5)
            plt.title(r'$\it{Smad7}$')
            plt.yticks([0, 1, 2, 3])
        elif gene_name == 'Klf10':
            plt.plot(sim.t, sim.Klf10_WT, color='brown', linewidth=1.5)
            plt.plot(sim.t, sim.Klf10_Smad2OE, color='royalblue', linewidth=1.5)
            plt.plot(sim.t, sim.Klf10_Smad3OE, color='darkgreen', linewidth=1.5)
            plt.plot(sim.t, sim.Klf10_Smad4OE, 'k', linewidth=1.5)
            plt.title(r'$\it{Klf10}$')
            plt.yticks([0, 2, 4])
        elif gene_name == 'Bmp4':
            plt.plot(sim.t, sim.Bmp4_WT, color='brown', linewidth=1.5)
            plt.plot(sim.t, sim.Bmp4_Smad2OE, color='royalblue', linewidth=1.5)
            plt.plot(sim.t, sim.Bmp4_Smad3OE, color='darkgreen', linewidth=1.5)
            plt.plot(sim.t, sim.Bmp4_Smad4OE, 'k', linewidth=1.5)
            plt.title(r'$\it{Bmp4}$')
            plt.yticks([0, 1, 2])
        elif gene_name == 'Cxcl15':
            plt.plot(sim.t, sim.Cxcl15_WT, color='brown', linewidth=1.5)
            plt.plot(sim.t, sim.Cxcl15_Smad2OE, color='royalblue', linewidth=1.5)
            plt.plot(sim.t, sim.Cxcl15_Smad3OE, color='darkgreen', linewidth=1.5)
            plt.plot(sim.t, sim.Cxcl15_Smad4OE, 'k', linewidth=1.5)
            plt.title(r'$\it{Cxcl15}$')
            plt.yticks([-1.5, -1, -0.5, 0, 0.5])
        elif gene_name == 'Dusp5':
            plt.plot(sim.t, sim.Dusp5_WT, color='brown', linewidth=1.5)
            plt.plot(sim.t, sim.Dusp5_Smad2OE, color='royalblue', linewidth=1.5)
            plt.plot(sim.t, sim.Dusp5_Smad3OE, color='darkgreen', linewidth=1.5)
            plt.plot(sim.t, sim.Dusp5_Smad4OE, 'k', linewidth=1.5)
            plt.title(r'$\it{Dusp5}$')
            plt.yticks([-1.5, -1, -0.5, 0])
        elif gene_name == 'Tgfa':
            plt.plot(sim.t, sim.Tgfa_WT, color='brown', linewidth=1.5)
            plt.plot(sim.t, sim.Tgfa_Smad2OE, color='royalblue', linewidth=1.5)
            plt.plot(sim.t, sim.Tgfa_Smad3OE, color='darkgreen', linewidth=1.5)
            plt.plot(sim.t, sim.Tgfa_Smad4OE, 'k', linewidth=1.5)
            plt.title(r'$\it{Tgfa}$')
            plt.yticks([-1.5, -1, -0.5, 0, 0.5])
        elif gene_name == 'Pdk4':
            plt.plot(sim.t, sim.Pdk4_WT, color='brown', linewidth=1.5)
            plt.plot(sim.t, sim.Pdk4_Smad2OE, color='royalblue', linewidth=1.5)
            plt.plot(sim.t, sim.Pdk4_Smad3OE, color='darkgreen', linewidth=1.5)
            plt.plot(sim.t, sim.Pdk4_Smad4OE, 'k', linewidth=1.5)
            plt.title(r'$\it{Pdk4}$')
            plt.yticks([-3, -2, -1, 0])

        if i >= 9:
            plt.xlabel('time (min)')
        plt.xticks([0, 200, 400, 600])
        if i % 3 == 0:
            plt.ylabel('gene expression(log2)')

    plt.savefig('TGFb_induced_expression.png', bbox_inches='tight')
