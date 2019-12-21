function initialValues_U2OS()
    u0 = zeros(V.len_f_vars);

    u0[V.p53] = 1
    u0[V.Mdm2] = 0.4
    u0[V.Wip1] = 0.3
    u0[V.ATMp] = 0

    return u0
end


function initialValues_MCF7()
    u0 = zeros(V.len_f_vars);

    u0[V.p53] = 1
    u0[V.Mdm2] = 1
    u0[V.Wip1] = 1
    u0[V.ATMp] = 0

    return u0
end