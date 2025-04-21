local o = io.read()
local t = {}
for i=1, 12 do
    t[i] = {}
    for j=1, 12 do
        local v = tonumber(io.read())
        t[i][j] = v
    end
end

local x = 12
local z = -1

local sum = 0

for i=2, 11 do
    for j=x, 12 do
        sum = sum + t[i][j]
    end
    if i == 6 then
        z = 0
    elseif i == 7 then
        z = 1
    end
    x = x + z
end

if o == 'S' then
    print(string.format('%.1f',sum))
else
    print(string.format('%.1f',sum / 30))
end