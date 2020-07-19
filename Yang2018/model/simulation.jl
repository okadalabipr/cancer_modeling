module Sim
include("./name2idx/parameters.jl")
include("./name2idx/species.jl")
include("./set_model.jl")

using .C
using .V
using Printf
using DelayDiffEq

const dt = 0.01

function solvedde(
        diffeq::Function,
        u0::Vector{Float64},
        history::Vector{Float64},
        tspan::Tuple{Float64,Float64},
        p::Vector{Float64},
        tau::Float64)
    h(p,t) = history
    lags = [tau]
    prob = DDEProblem(diffeq,u0,h,tspan,p;constant_lags=lags)
    alg = MethodOfSteps(BS3())
    sol = solve(prob,alg,saveat=dt)
    return sol
end

const tspan = (0.0,48.0)
const t = collect(tspan[1]:dt:tspan[end])

const n_condition = 4

p53_conc = Matrix{Float64}(undef, length(t), n_condition)

for i in 1:n_condition
    local p::Vector{Float64}
    local u0::Vector{Float64}

    if i == 1
        p = param_values_U2OS()
        u0 = initialValues_U2OS()
        p[C.Eto] = 1
    elseif i == 2
        p = param_values_U2OS()
        u0 = initialValues_U2OS()
        p[C.Eto] = 100
    elseif i == 3
        p = param_values_MCF7()
        u0 = initialValues_MCF7()
        p[C.Eto] = 5
    elseif i == 4
        p = param_values_MCF7()
        u0 = initialValues_MCF7()
        p[C.Eto] = 200
    end

    sol = solvedde(diffeq,u0,u0,tspan,p,2.1)
    for j in eachindex(t)
        p53_conc[j,i] = sol.u[j][V.p53]
    end
end

end  # module
