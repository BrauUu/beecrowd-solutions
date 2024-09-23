local entry = io.read()
local t = {}

for v in string.gmatch(entry, "[^%s]+") do
    table.insert(t, tonumber(v))
end

local a = t[1]
local b = t[2]
local c = t[3]

if a + b > c and b + c > a and a + c > b then
    print('Perimetro = '..string.format('%.1f', a+b+c))
else
    print('Area = '..string.format('%.1f', ((a+b)*c)/2))
end
