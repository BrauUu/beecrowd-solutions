local options = {
    [1] = 'A',
    [2] = 'B',
    [3] = 'C',
    [4] = 'D',
    [5] = 'E'
}

while true do
    local n = tonumber(io.read())
    if n == 0 then
        break
    end
    for i = 1, n do
        local entry = io.read()
        local t = {}
        for v in string.gmatch(entry, '%S+') do
            table.insert(t, tonumber(v))
        end
        local chosenOptions = {}
        for index, value in pairs(t) do
            if value <= 127 then
                table.insert(chosenOptions, index)
            end
        end
        if #chosenOptions ~= 1 then
            print('*')
        else
            print(options[chosenOptions[1]])
        end
    end
end