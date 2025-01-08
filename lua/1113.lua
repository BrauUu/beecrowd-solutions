while true do
    local entry = io.read()
    local t = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(t, tonumber(v))
    end
    if t[1] == t[2] then
        break
    elseif t[1] > t[2] then
        print('Decrescente')
    else
        print('Crescente')
    end
end