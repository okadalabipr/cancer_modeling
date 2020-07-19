function kmp(p,ATMp,Wip1) 
    return p[C.kmp0]*(p[C.Dp0]+p[C.Dwp]*Wip1)/(p[C.Sp0]+p[C.Dp0]+p[C.Sap]*ATMp+p[C.Dwp]*Wip1)
end

function Kpm(p,ATMp,Wip1)
    return p[C.Kpm0]*(p[C.Sp0]+p[C.Dp0]+p[C.Sap]*ATMp+p[C.Dwp]*Wip1)/(p[C.Sp0]+p[C.Sap]*ATMp)
end

function Kpw(p,ATMp,Wip1)
    return p[C.Kpw0]*(p[C.Sp0]+p[C.Dp0]+p[C.Sap]*ATMp+p[C.Dwp]*Wip1)/(p[C.Sp0]+p[C.Sap]*ATMp)
end

function γm(p,ATMp,Wip1,γm0,γm1)
    return (γm0*(p[C.Dm0]+p[C.Dwm]*Wip1)+γm1*(p[C.Sm0]+p[C.Sam]*ATMp))/(p[C.Sm0]+p[C.Dm0]+p[C.Sam]*ATMp+p[C.Dwm]*Wip1)
end


function diffeq(du,u,h,p,t)

    du[V.p53] = p[C.kp0] - kmp(p,u[V.ATMp],u[V.Wip1])*u[V.p53]*u[V.Mdm2] - p[C.γp]*u[V.p53];

    du[V.Mdm2] = p[C.km0] + p[C.kpm]*(h(p,t-p[C.τm])[V.p53]^p[C.nm])/(Kpm(p,h(p,t-p[C.τm])[V.ATMp],h(p,t-p[C.τm])[V.Wip1])^p[C.nm]+h(p,t-p[C.τm])[V.p53]^p[C.nm]) - γm(p,u[V.ATMp],u[V.Wip1],p[C.γm0],p[C.γm1])*u[V.Mdm2];

    du[V.Wip1] = p[C.kw0] + p[C.kpw]*(h(p,t-p[C.τw])[V.p53]^p[C.nw])/(Kpw(p,h(p,t-p[C.τw])[V.ATMp],h(p,t-p[C.τw])[V.Wip1])^p[C.nw]+h(p,t-p[C.τw])[V.p53]^p[C.nw]) - p[C.γw]*u[V.Wip1];

    du[V.ATMp] = p[C.Sea]*p[C.Eto]*(p[C.ATMt] - u[V.ATMp]) - p[C.Da0]*u[V.ATMp];
    
end


function param_values_U2OS()
    p = zeros(C.NUM)

    p[C.kp0] = 1.3396
    p[C.km0] = 0.08
    p[C.kw0] = 0.105
    p[C.kpm] = 0.9172
    p[C.kpw] = 0.1496
    p[C.nm] = 4
    p[C.nw] = 4
    p[C.Kpm0] = 0.4025
    p[C.Kpw0] = 0.4025
    p[C.τm] = 2.1
    p[C.τw] = 2.1
    p[C.kmp0] = 4.038
    p[C.γp] = 0.1
    p[C.γm0] = 0.2579
    p[C.γm1] = 7.7362
    p[C.γw] = 0.4
    p[C.Sea] = 1
    p[C.Da0] = 80
    p[C.Sp0] = 0.25
    p[C.Sap] = 0.8335
    p[C.Dp0] = 0.75
    p[C.Dwp] = 0.25
    p[C.Sm0] = 0.0153
    p[C.Sam] = 0.283
    p[C.Dm0] = 0.5
    p[C.Dwm] = 0.5
    p[C.ATMt] = 16

    return p
end


function param_values_MCF7()
    p = zeros(C.NUM)

    p[C.kp0] = 2.4138
    p[C.km0] = 0.2
    p[C.kw0] = 0.35
    p[C.kpm] = 2.3854
    p[C.kpw] = 0.8702
    p[C.nm] = 4
    p[C.nw] = 4
    p[C.Kpm0] = 0.4025
    p[C.Kpw0] = 0.4025
    p[C.τm] = 2.1
    p[C.τw] = 2.1
    p[C.kmp0] = 2.7048
    p[C.γp] = 0.25
    p[C.γm0] = 0.1804
    p[C.γm1] = 3.6088
    p[C.γw] = 0.4
    p[C.Sea] = 1
    p[C.Da0] = 30
    p[C.Sp0] = 0.25
    p[C.Sap] = 0.4335
    p[C.Dp0] = 0.75
    p[C.Dwp] = 0.25
    p[C.Sm0] = 0.0479
    p[C.Sam] = 0.2830
    p[C.Dm0] = 0.5
    p[C.Dwm] = 0.5
    p[C.ATMt] = 3.5

    return p
end


function initialValues_U2OS()
    u0 = zeros(V.NUM)

    u0[V.p53] = 1
    u0[V.Mdm2] = 0.4
    u0[V.Wip1] = 0.3
    u0[V.ATMp] = 0

    return u0
end


function initialValues_MCF7()
    u0 = zeros(V.NUM)

    u0[V.p53] = 1
    u0[V.Mdm2] = 1
    u0[V.Wip1] = 1
    u0[V.ATMp] = 0

    return u0
end