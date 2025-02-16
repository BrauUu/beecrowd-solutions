local o = io.read()
local t = {}
for i=1, 12 do
    t[i] = {}
    for j=1, 12 do
        local v = tonumber(io.read())
        t[i][j] = v
    end
end

local x = 1
local y = 12

local sum = 0

for i=1, 5 do
    x = x + 1
    y = y - 1
    for j=x, y do
        sum = sum + t[i][j]
    end
end

if o == 'S' then
    print(string.format('%.1f',sum))
else
    print(string.format('%.1f',sum / 30))
end