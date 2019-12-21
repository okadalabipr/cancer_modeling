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