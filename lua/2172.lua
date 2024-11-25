while true do
    local entry = io.read()
    local t = {}
    for value in string.gmatch(entry, "[^%s]+") do
        table.insert(t, tonumber(value))
    end
    local x = t[1]
    local xp = t[2]
    if x == 0 and xp == 0 then
        break
    end
    print(xp*x)
end
