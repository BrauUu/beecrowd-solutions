local entry = io.read()
local t = {}
for v in string.gmatch(entry, "[^%s]+") do
    table.insert(t, tonumber(v))
end
local a = t[1]
local b = t[2]
local c = t[3]
local d = t[4]
if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0 then
    print("Valores aceitos")
else
    print("Valores nao aceitos")
end