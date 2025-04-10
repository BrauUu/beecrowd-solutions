while true do
    local entry = io.read()
    local t = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(t, tonumber(v))
    end
    table.sort(t)
    local a = t[1]
    local b = t[2]
    if a == 0 and b == 0 then
        break
    end
    local c = ((-a + -b)/3+a)*3
    print(string.format("%0.f", c))
end