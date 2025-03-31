local n = tonumber(io.read())

for i=1,n do
    local text = io.read()
    local newText = ''
    for g=1, #text do
        local char = string.sub(text, g, g)
        if string.match(char, '[a-zA-Z]') then
            char = string.char(string.byte(char) + 3)
        end
        newText = newText..char
    end
    newText = string.reverse(newText)
    text = string.sub(newText, 1, math.floor(#newText/ 2))
    for g = math.ceil(#newText/ 2 + 0.5), #newText do
        local char = string.sub(newText, g, g)
        char = string.char(string.byte(char) - 1)
        text = text..char
    end
    print(text)
end