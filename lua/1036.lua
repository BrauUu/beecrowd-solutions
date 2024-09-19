local entry = io.read()
local t = {}
for value in string.gmatch(entry, "[^%s]+") do
    table.insert(t, tonumber(value))
end

local a = t[1]
local b = t[2]
local c = t[3]
local delta = b^2 - 4 * a * c

if delta >= 0 and a > 0 then
    local r1 = (-b + math.sqrt(delta))/(2 * a)
    local r2 = (-b - math.sqrt(delta))/(2 * a)
    print('R1 = '..string.format("%.5f", r1))
    print('R2 = '..string.format("%.5f", r2))
else
    print('Impossivel calcular')
end
