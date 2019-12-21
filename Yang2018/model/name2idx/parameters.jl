module C
const param_names = [
    "kp0"   # Basal production rate of p53
    "km0"   # Basal production rate of Mdm2
    "kw0"   # Basal production rate of Wip1
    "kpm"   # Rate constant of p53p-induced production of Mdm2
    "kpw"   # Rate constant of p53p-induced production of Wip1
    "nm"    # Hill coefficient of p53p-induced production of Mdm2
    "nw"    # Hill coefficient of p53p-induced production of Wip1
    "Kpm0"  # Michaelis constant for p53p-induced production of Mdm2
    "Kpw0"  # Michaelis constant for p53p-induced production of Wip1
    "τm"    # Time delay in production of Mdm2
    "τw"    # Time delay in production of Wip1
    "kmp0"  # Rate constant of Mdm2-induced degradation of p53u
    "γp"    # Mdm2-independent degradation rate constant of p53
    "γm0"   # Degradation rate constant of Mdm2u
    "γm1"   # Degradation rate constant of Mdm2p
    "γw"    # Degradation rate constant of Wip1
    "Sea"   # Rate constant of etoposide-induced phosphorylation of ATM
    "Da0"   # Rate constant of dephosphorylation of ATM
    "Sp0"   # Rate constant of ATM-independent phosphorylation of p53
    "Sap"   # Rate constant of ATM-mediated phosphorylation of p53
    "Dp0"   # Rate constant of Wip1-independent dephosphorylation of p53
    "Dwp"   # Rate constant of Wip1-mediated dephosphorylation of p53
    "Sm0"   # Rate constant of ATM-independent phosphorylation of Mdm2
    "Sam"   # Rate constant of ATM-mediated phosphorylation of Mdm2
    "Dm0"   # Rate constant of Wip1-independent dephosphorylation of Mdm2
    "Dwm"   # Rate constant of Wip1-mediated dephosphorylation of Mdm2
    "ATMt"  # Total amount of ATM
    #
    "Eto"   # Etoposide
];

for (idx,name) in enumerate(param_names)
    eval(Meta.parse("const $name = $idx"));
end

const len_f_params = length(param_names);

end  # module