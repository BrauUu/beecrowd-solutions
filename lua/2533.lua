local function main()
    local n = tonumber(io.read())
    local sumNxC = 0
    local sumC = 0

    for i=1,n do
        local entry = io.read()
        local temp = {}
        for v in string.gmatch(entry, '[^%s]+') do
            table.insert(temp, tonumber(v))
        end
        local grade = temp[1]
        local workload = temp[2]
        sumNxC = sumNxC + (grade*workload)
        sumC = sumC + workload
    end

    local ira = sumNxC / (sumC * 100)
    print(string.format("%.4f", ira))
end

while true do
    if not pcall(main) then
        break
    end
end