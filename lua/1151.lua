local n = tonumber(io.read())

local sequence = {0, 1}
local res = '0 1'

for i=3, n do
    local value = sequence[i-2] + sequence[i-1]
    table.insert(sequence, value)
    res = res..' '..tonumber(value)
end

if n > 1 then
    print(res)
else
    print('0')
end
