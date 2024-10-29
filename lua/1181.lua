local t = {}

local line = io.read("n")
local _ = io.read()
local operation = io.read()

for i = 0, 11, 1 do
    t[i] = {}
    for j = 0, 11, 1 do
        t[i][j] = io.read("n")
    end
end

local sum = 0

for i = 0, 11, 1 do
   sum = sum + t[line][i]
end

if operation == 'S' then
    print(string.format("%.1f", sum))
elseif operation == 'M' then
    print(string.format("%.1f", sum/12))
end