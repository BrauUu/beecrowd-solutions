local entry = io.read()
local t = {}
for value in string.gmatch(entry, "[^%s]+") do
    table.insert(t, value)
end
local A = t[1]
local B = t[2]
local C = t[3]

local temp = (A+B+math.abs(A-B))/2
local bigger = (temp+C+math.abs(temp-C))/2

print(string.format("%d", bigger).." eh o maior")