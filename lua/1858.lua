local n = io.read('n')
_ = io.read()

local t = {}
local entry = io.read()

for v in string.gmatch(entry, "[^%s]+") do
    table.insert(t, tonumber(v))
end

local smlst = 21
local num
for ind, value in ipairs(t) do
    if value < smlst then
        smlst = value
        num = ind
    end
end

print(num)