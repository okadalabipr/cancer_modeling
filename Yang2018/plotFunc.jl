function plotFunc_timecourse(Sim::Module)
    rc("figure",figsize = (10.5,4));
    rc("font",family = "Arial");
    rc("font",size = 12);
    rc("axes",linewidth = 1);
    rc("lines",linewidth = 2);

    subplot(1,2,1);
    plot(Sim.t,Sim.p53_conc[:,1],"k",label="1μM etoposide");
    plot(Sim.t,Sim.p53_conc[:,2],"r",label="100μM etoposide");
    xlim(0,48);
    xticks([0,12,24,36,48]);
    ylim(0,8);
    yticks([1,3,5,7]);
    xlabel("Time (hours)");
    ylabel("[p53]");
    legend(loc="upper right",frameon=false);
    text(1,7.5,"U-2 OS");

    subplot(1,2,2);
    plot(Sim.t,Sim.p53_conc[:,3],"k",label="5μM etoposide");
    plot(Sim.t,Sim.p53_conc[:,4],"r",label="200μM etoposide");
    xlim(0,48);
    xticks([0,12,24,36,48]);
    ylim(0,5.5);
    yticks([0,1,2,3,4,5]);
    xlabel("Time (hours)");
    ylabel("[p53]");
    legend(loc="upper right",frameon=false);
    text(1,5.15,"MCF7")
    
    show();

end
