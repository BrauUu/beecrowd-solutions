local n = tonumber(io.read())

for i=1, n do
    local m = tonumber(io.read())
    local fruits = {}
    local totalPrice = 0
    for j=1, m do
        local entry = io.read()
        local temp = {}
        for value in string.gmatch(entry, '[^%s]+') do
            table.insert(temp, value)
        end
        fruits[temp[1]] = temp[2]
    end
    local p = tonumber(io.read())
    for j=1, p do
        local entry = io.read()
        local temp = {}
        for value in string.gmatch(entry, '[^%s]+') do
            table.insert(temp, value)
        end
        local price = fruits[temp[1]]
        totalPrice = totalPrice + (price * tonumber(temp[2]))
    end
    print(string.format('R$ %.2f', totalPrice))
end