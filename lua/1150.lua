local x = tonumber(io.read())
local z = x - 1
while z <= x do
    z = tonumber(io.read())
end

local sum = x
local count = 1
while sum <= z do
    sum = sum + x + count
    count = count + 1
end

print(count)