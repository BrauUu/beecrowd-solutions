local entry = io.read()
local t = {}
for v in string.gmatch(entry, "%S+") do
    table.insert(t, tonumber(v))
end

local a = t[1]
local b = t[2]
local c = t[3]
local d = t[4]

local x = (a * d) + (c * b)
local y = (b * d)

for i = y, 1, -1 do
    if x % i == 0 and y % i == 0 then
        x = x // i
        y = y // i
        break
    end
end

print(x.." "..y)