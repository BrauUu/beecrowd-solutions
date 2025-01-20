local n = tonumber(io.read())

for i=1,n do
    local entry = io.read()
    local temp = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(temp, tonumber(v))
    end
    local x = temp[1]
    local y = temp[2]

    if y ~= 0 then
        print(string.format('%.1f', x/y))
    else
        print('divisao impossivel')
    end
end