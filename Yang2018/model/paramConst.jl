function f_params_U2OS()
    p = zeros(C.len_f_params);

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


function f_params_MCF7()
    p = zeros(C.len_f_params);

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