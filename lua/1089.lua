while true do
    local n = tonumber(io.read())
    if n == 0 then
        break
    end
    local entry = io.read()
    local sample = {}
    for v in entry:gmatch("%S+") do
        table.insert(sample, tonumber(v))
    end
    local count = 0
    for key, v in ipairs(sample) do
        local twoValuesBack
        local oneValueBack
        if sample[key - 2] then
            twoValuesBack = sample[key - 2]
        else
            twoValuesBack = sample[#sample - (2-key)]
        end
        if sample[key - 1] then
            oneValueBack = sample[key - 1]
        else
            oneValueBack = sample[#sample]
        end
        if (twoValuesBack > oneValueBack and v > oneValueBack) or (twoValuesBack < oneValueBack and v < oneValueBack) then
            count = count + 1
        end
    end
    print(count)
end