local entry = io.read()
local temp = {}
for v in string.gmatch(entry, '%S+') do
    table.insert(temp, tonumber(v))
end
local n = temp[1]
local m = temp[2]

local field = {}
for i=1, n do
    entry = io.read()
    temp = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(temp, tonumber(v))
    end
    table.insert(field, temp)
end

local sumXTable = {}
local sumYTable = {}

for i=1, n do
    for j=1, m do
        sumXTable[i] = field[i][j] + (sumXTable[i] or 0)
        sumYTable[j] = field[i][j] + (sumYTable[j] or 0)
    end
end

table.sort(sumXTable, function (a, b)
    if a > b then
        return a
    end
    return b
end)
table.sort(sumYTable, function (a, b)
    if a > b then
        return a
    end
    return b
end)

if sumXTable[1] > sumYTable[1] then
    print(sumXTable[1])
else
    print(sumYTable[1])
end