local n = tonumber(io.read())

for i=1, n do
    local str = io.read()
    local num = tonumber(io.read())
    local cypher = ''
    for j=1, #str do
        local char = string.sub(str, j, j)
        local code = string.byte(char)
        local newCode = (code - num)
        if newCode < 65 then
            newCode = 91 - (65 - newCode)
        end
        cypher = cypher..string.char(newCode)
    end
    print(cypher)
end