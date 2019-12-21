module Yang2018
using PyPlot;

export runSim

include("model/model.jl");
using .Model;

include("simulation.jl");
using .Sim;

include("plotFunc.jl");

function runSim()
    plotFunc_timecourse(Sim);
end

end  # module