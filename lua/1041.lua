local entry = io.read()
local t = {}
for value in string.gmatch(entry, '[^%s]+') do
    table.insert(t, tonumber(value))
end

local x = t[1]
local y = t[2]

if x > 0 and y > 0 then
    print('Q1')
elseif x < 0 and y > 0 then
    print('Q2')
elseif x < 0 and y < 0 then
    print('Q3')
elseif x > 0 and y < 0 then
    print('Q4')
elseif x == 0 and y == 0 then
    print('Origem')
elseif x == 0 then
    print('Eixo Y')
elseif y == 0 then
    print('Eixo X')
end