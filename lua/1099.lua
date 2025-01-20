local n = tonumber(io.read())

for i=1, n do
    local entry = io.read()
    local temp = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(temp, tonumber(v))
    end

    local x
    local y

    if temp[1] < temp[2] then
        x = temp[1]
        y = temp[2]
    else
        x = temp[2]
        y = temp[1]
    end

    local sum = 0
    for j=x + 1, y - 1 do
        if j % 2 == 1 then
            sum = sum + j
        end
    end
    print(sum)
end