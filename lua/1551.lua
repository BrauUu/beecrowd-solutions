local n = tonumber(io.read())

for i=1,n do
    local phrase = io.read()
    local count = 0
    for j=97,122  do
        local char = string.char(j)
        local ind = string.find(phrase, char)
        if ind then
            count = count + 1
        end
    end
    if count == 26 then
        print('frase completa')
    elseif count >= 13 then
        print('frase quase completa')
    else
        print('frase mal elaborada')
    end
end