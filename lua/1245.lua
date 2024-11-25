local function main()
    local n = tonumber(io.read())
    local left = {}
    local right = {}
    for i = 1, n do
        local entry = io.read()
        local temp = {}
        for value in string.gmatch(entry, "[^%s]+") do
            table.insert(temp, value)
        end
        local size = temp[1]
        local side = temp[2]
        if side == 'D' then
            local count = 0
            if right[size] then
                count = right[size]
            end
            right[size] = count + 1
        else
            local count = 0
            if left[size] then
                count = left[size]
            end
            left[size] = count + 1
        end
    end
    local count = 0
    for key, value in pairs(right) do
        local lValue = 0
        if left[key] then
            lValue = left[key]
        end
        if value < lValue then
            count = count + value
        else
            count = count + lValue
        end
    end
    print(count)
end

while true do
    if not pcall(main) then
        break
    end
end
