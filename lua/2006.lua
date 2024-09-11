local t = io.read('n')
io.read()
local entry = io.read()

local count = 0

for v in string.gmatch(entry, "[^%s]+") do
    if tonumber(v) == t then
        count = count + 1
    end
end
print(count)