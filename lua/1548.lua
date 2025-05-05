local n = tonumber(io.read())

for _ = 1, n do
    local m = tonumber(io.read())
    local p = io.read()
    local t = {}
    local newT = {}
    for value in string.gmatch(p, '%S+') do
        table.insert(t, tonumber(value))
        table.insert(newT, tonumber(value))
    end
    
    local count = 0
    table.sort(t, function (a, b)
        return a > b
    end)

    for ind,item in pairs(newT) do
        if item == t[ind] then
            count = count + 1
        end
    end
    print(count)
end