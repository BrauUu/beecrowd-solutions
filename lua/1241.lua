local n = tonumber(io.read())

for i=1,n do
    local entry = io.read()
    local temp = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(temp, v)
    end
    local a = temp[1]
    local b = temp[2]
    if string.sub(a, #a - #b + 1, #a) == b then
        print('encaixa')
    else
        print('nao encaixa')
    end
end