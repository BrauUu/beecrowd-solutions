local n = tonumber(io.read())

for _ = 1, n do
    local entry = io.read()
    local t = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(t, tonumber(v))
    end
    
    local x = t[1]
    local y = t[2]
    
    local i
    local sum = 0
    if x % 2 == 1 then
        i = x
    else
        i = x + 1
    end
    for j = 1, y do
        sum = sum + i
        i = i + 2
    end
    print(sum)
end