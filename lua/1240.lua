local n = tonumber(io.read())

for _ = 1, n do
    local entry = io.read()
    local t = {}
    for value in string.gmatch(entry, "%S+") do
        table.insert(t, value)
    end
    local a  = t[1]
    local b  = t[2]

    if a:sub(#a - #b + 1) == b then
        print('encaixa')
    else
        print('nao encaixa')
    end
end
