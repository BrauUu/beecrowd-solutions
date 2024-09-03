local entry1 = io.read()
local entry2 = io.read()
local entry = entry1.." "..entry2

local t = {}

for num in string.gmatch(entry, "[^%s]+") do
   table.insert(t, num) 
end

local distance = math.sqrt((t[3] - t[1])^2 + (t[4] - t[2])^2)

print(string.format("%.4f", distance))