local function main()
    local entry = io.read()
    local temp = {}

    for v in string.gmatch(entry, '[^%s]+') do
        table.insert(temp, tonumber(v))
    end

    local startNum = temp[1]
    local endNum = temp[2]
    local totalCount = 0

    for num = startNum, endNum do
        num = tostring(num)
        local count = 1
        for i=1, #num do
            local char = string.sub(num, i, i)
            for j=i+1, #num do
                local tempChar = string.sub(num, j, j)
                if tempChar == char then
                    count = count + 1
                end
            end
        end
        if count > 1 then
            totalCount = totalCount + 1
        end
    end
    print(endNum - startNum + 1 - totalCount)
end

while true do
    if not pcall(main) then
        break
    end
end