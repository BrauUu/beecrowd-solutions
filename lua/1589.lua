local n = tonumber(io.read())

for i=1, n do
    local entry = io.read()
    local temp = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(temp, tonumber(v))
    end

    print(temp[1] + temp[2])
end