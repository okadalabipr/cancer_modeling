module V
const NAMES = [
    "p53"
    "Mdm2"
    "Wip1"
    "ATMp"
]

for (idx,name) in enumerate(NAMES)
    eval(Meta.parse("const $name = $idx"))
end

const NUM = length(NAMES)

end  # module