local n = tonumber(io.read())
local sum = 0

for i=1, n do
    local entry = io.read()
    local temp = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(temp, tonumber(v))
    end
    local l = temp[1]
    local c = temp[2]
    if l > c then
        sum = sum + c
    end
end
print(sum)