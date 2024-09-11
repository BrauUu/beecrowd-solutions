local entry = io.read()

local t = {}
local sortedT = {}

for v in string.gmatch(entry, "[^%s]+") do
    table.insert(t, tonumber(v))
    table.insert(sortedT, tonumber(v))
end
 	
table.sort(t)

for i = 1,3,1   do
    print(t[i])
end

print()

for i = 1,3,1   do
    print(sortedT[i])
end
