while true do
    local entry = io.read()
    local temp = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(temp, tonumber(v))
    end
    if temp[1] <= 0 or temp[2] <= 0 then
        break
    end

    local m
    local n

    if temp[1] > temp[2] then
        m = temp[1]
        n = temp[2]
    else
        n = temp[1]
        m = temp[2]
    end
    local res = ''
    local sum = 0
    for i=n,m do
        res = res..tostring(i)..' '
        sum = sum + i
    end
    print(string.format('%sSum=%i', res, sum))
end