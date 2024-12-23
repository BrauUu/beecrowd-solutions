while true do
    local n = tonumber(io.read())
    if n == 0 then
        break
    end
    local rods = {}
    for i=1, n do
        local entry = io.read()
        local temp = {}
        for v in string.gmatch(entry, '%S+') do
            table.insert(temp, tonumber(v))
        end
        local x = temp[2]
        table.insert(rods, x)
    end
    local wholeCount = 0
    local halfCount = 0
    for _, rodsCount in pairs(rods) do
        wholeCount = wholeCount + (rodsCount // 4)
        local rest = rodsCount % 4
        halfCount = halfCount + (rest // 2)
    end
    wholeCount = wholeCount + (halfCount // 2)
    print(wholeCount)
end