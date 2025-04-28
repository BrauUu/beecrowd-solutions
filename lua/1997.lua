while true do
    local entry = io.read()
    local tab = {}
    for value in string.gmatch(entry, "%S+") do
        table.insert(tab, value)
    end
    local t = tab[2]
    local s = tab[1]
    if t == '*' and s == '*' then
        break
    end
    local count = 0
    local flag = false

    for i = 1, #t do
        if t:sub(i, i) ~= s:sub(i, i) then
            flag = true
            goto continue
        end
        if flag then
            flag = false
            count = count + 1
        end
        ::continue::
    end
    if flag then
        count = count + 1
    end
    print(count)
end
