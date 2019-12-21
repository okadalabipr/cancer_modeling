module Model

export 
    C,
    V,
    f_params_U2OS,
    f_params_MCF7,
    initialValues_U2OS,
    initialValues_MCF7,
    diffeq

include("name2idx/name2idx.jl");
using .Name2Idx;

include("paramConst.jl");
include("initialCondition.jl");
include("differentialEquation.jl");

end  # module