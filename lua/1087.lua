while true do
    local entry = io.read()
    local t = {}
    for v in string.gmatch(entry, "[^%s]+") do
        table.insert(t, tonumber(v))
    end

    local x1 = t[1]
    local y1 = t[2]
    local x2 = t[3]
    local y2 = t[4]

    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0 then
        break
    end

    local actualX = x1
    local actualY = y1

    local moveCount = 0
    while actualX ~= x2 or actualY ~= y2 do
        if actualX == x2 then
            actualY = y2
        elseif y2 == actualY then
            actualX = x2
        else
            local x
            local y
            local smallest
            local xDiff = math.abs(x2 - actualX)
            local yDiff = math.abs(y2 - actualY)
            if actualX < x2 then
                x = 1
            else
                x = -1
            end
            if actualY < y2 then
                y = 1
            else
                y = -1
            end

            if xDiff < yDiff then
                smallest = xDiff
            else
                smallest = yDiff
            end
            actualX = actualX + x * smallest
            actualY = actualY + y * smallest
        end
        moveCount = moveCount + 1
    end
    print(moveCount)
end