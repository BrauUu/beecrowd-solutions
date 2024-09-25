local entry = io.read()
local t = {}
for v in string.gmatch(entry, '[^%s]+') do
    table.insert(t, tonumber(v))
end

table.sort(t, function (a, b) return a > b end)

local a = t[1]
local b = t[2]
local c = t[3]

if a >= b + c then
    print('NAO FORMA TRIANGULO')
else
    if a^2 == b^2 + c^2 then
    print('TRIANGULO RETANGULO')
    end

    if a^2 > b^2 + c^2 then
        print('TRIANGULO OBTUSANGULO')
    end

    if a^2 < b^2 + c^2 then
        print('TRIANGULO ACUTANGULO')
    end

    if a == b and a == c then
        print('TRIANGULO EQUILATERO')
    elseif a == b or b == c or c == a then
        print('TRIANGULO ISOSCELES')
    end
end