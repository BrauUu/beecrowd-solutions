local entry = io.read()
local temp = {}
for v in string.gmatch(entry, '%S+') do
    table.insert(temp, tonumber(v))
end

if temp[1] < temp[2] and temp[1] < temp[3] then
    print('Otavio')
elseif temp[2] < temp[3] and temp[2] < temp[1] then
    print('Bruno')
elseif temp[3] < temp[1] and temp[3] < temp[2] then
    print('Ian')
else
    print('Empate')
end