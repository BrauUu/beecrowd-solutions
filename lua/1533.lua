while true do
    local n = tonumber(io.read())
    if n == 0 then
        break
    end
    local entry = io.read()
    local greatest = 0
    local greatestIndex = 0
    local secondGreatest = 0
    local secondGreatestIndex = 0
    local i = 1
    for v in entry:gmatch('%S+') do
        v = tonumber(v)
        if v > greatest then
            secondGreatest = greatest
            secondGreatestIndex = greatestIndex
            greatest = v
            greatestIndex = i
        elseif v > secondGreatest then
            secondGreatest = v
            secondGreatestIndex = i
        end
        i = i + 1
    end
    print(secondGreatestIndex)
end
