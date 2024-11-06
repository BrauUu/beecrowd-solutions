while true do
    local entry = io.read()
    local t = {}
    for v in string.gmatch(entry, "[^%s]+") do
        table.insert(t, tonumber(v))
    end

    local startHour = t[1]
    local startMin = t[2]
    local endHour = t[3]
    local endMin = t[4]

    if startHour == 0 and startMin == 0 and endHour == 0 and endMin == 0 then
        break
    end

    local startTotalMinutes = startHour * 60 + startMin
    local endTotalMinutes = endHour * 60 + endMin
    local diff = endTotalMinutes - startTotalMinutes

    if diff < 0 then
        diff = 1440 + diff
    end

    print(diff)
end