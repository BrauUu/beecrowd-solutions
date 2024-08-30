local t = {}
local i = 0
for j = 0,1,1 do
    local entry = io.read()
    for value in string.gmatch(entry, "[^%s]+") do
        t[i] = value
        i = i + 1
    end
end

local total = t[1] * t[2] + t[4] * t[5]

print("VALOR A PAGAR: R$ "..string.format("%.2f", total))