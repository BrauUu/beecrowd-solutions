local n = tonumber(io.read())
local evens = {}
local odds = {}
for i=1,n do
    local value = tonumber(io.read())
    if value % 2 == 0 then
        table.insert(evens, value)
    else
        table.insert(odds, value)
    end
end

table.sort(evens)
table.sort(odds)

for _, value in pairs(evens) do
    print(value)
end
for i=#odds, 1, -1 do
    print(odds[i])
end