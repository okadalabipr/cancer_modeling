module V
const var_names = [
    "p53"
    "Mdm2"
    "Wip1"
    "ATMp"
];

for (idx,name) in enumerate(var_names)
    eval(Meta.parse("const $name = $idx"));
end

const len_f_vars = length(var_names);

end  # module