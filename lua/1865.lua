local n = io.read('n')
local _ = io.read()

for i=1, n do
    local entry = io.read()
    local t = {}
    for v in string.gmatch(entry, "[^%s]+") do
        table.insert(t, v)
    end
    local name = t[1]
    local force = t[2]

    if name == 'Thor' then
        print('Y')
    else
        print('N')
    end
end