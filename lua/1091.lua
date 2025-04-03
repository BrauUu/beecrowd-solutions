local function getTerritory(n,m,x,y)
    if x == n or y == m then
        return 'divisa'
    end
    if x > n and y > m then
        return 'NE'
    end
    if x < n and y > m then
        return 'NO'
    end
    if x > n and y < m then
        return 'SE'
    end
    if x < n and y < m then
        return 'SO'
    end
end

while true do
    local k = tonumber(io.read())
    if k == 0 then
        break
    end
    local entry = io.read()
    local t = {}
    for value in string.gmatch(entry, "[^%s]+") do
        table.insert(t, tonumber(value))
    end
    local n = t[1]
    local m = t[2]
    for i = 1, k do
        entry = io.read()
        t = {}
        for value in string.gmatch(entry, "[^%s]+") do
            table.insert(t, tonumber(value))
        end
        local x = t[1]
        local y = t[2]
        print(getTerritory(n,m,x,y))
    end
end
