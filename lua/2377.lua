local entry = io.read()
entry = entry..' '..io.read()
local temp = {}

for v in string.gmatch(entry, '%S+') do
    table.insert(temp, tonumber(v))
end

local l = temp[1]
local d = temp[2]
local k = temp[3]
local p = temp[4]

local totalCost = (l // d) * p + (k*l)

print(totalCost)