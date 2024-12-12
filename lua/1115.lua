while true do
    local entry = io.read()
    local temp = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(temp, tonumber(v))
    end
    local x = temp[1] 
    local y = temp[2]
    if x == 0 or y == 0 then
        break
    end

    if x > 0 and y > 0 then
        print('primeiro')
    elseif x < 0 and y > 0 then
        print('segundo')
    elseif x < 0 and y < 0 then
        print('terceiro')
    elseif x > 0 and y < 0 then
        print('quarto')
    end

end