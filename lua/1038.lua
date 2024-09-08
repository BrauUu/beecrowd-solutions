local products = {
    [1] = {"Cachorro Quente", 4.00},
    [2] = {"X-Salada", 4.50},
    [3] = {"X-Bacon", 5.00},
    [4] = {"Torrada simples", 2.00},
    [5] = {"Refrigerante", 1.50},
}

local entry = io.read()
local t = {}

for v in string.gmatch(entry, "[^%s]+") do
    table.insert(t, v)
end

local id = tonumber(t[1])
local qty = tonumber(t[2])

local total = products[id][2] * qty

print("Total: R$ "..string.format("%.2f", total))