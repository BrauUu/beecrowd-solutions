local n = tonumber(io.read())

for i=1, n do
    local entry = io.read()
    local t = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(t, tonumber(v))
    end
    print(string.format('%.1f', ((t[1] * 2) + (t[2] * 3) + (t[3] * 5))/10))
end