local n = tonumber(io.read())
local char = io.read()

local t = {}
local sum = 0

for i=1, 12 do
    t[i] = {}
    for j=1, 12 do
        t[i][j] = tonumber(io.read())
        if j - 1 == n then
            sum = sum + t[i][j]
        end
    end
end

if char == 'M' then
    print(string.format('%.1f', sum / 12))
else
    print(string.format('%.1f', sum))
end