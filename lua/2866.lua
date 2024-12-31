local n = tonumber(io.read())

for i=1, n do
    local c = io.read()
    local text = ''
    for j=1, #c do
        local char = string.sub(c,j,j)
        if string.lower(char) == char then
            text = char..text
        end
    end
    print(text)
end