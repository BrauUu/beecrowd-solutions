local entry = io.read()
local temp = {}
for v in string.gmatch(entry, '%S+') do
    table.insert(temp, tonumber(v))
end

if temp[3] / temp[1] > temp[4] / temp[2] then
    print('A')
else
    print('G')
end