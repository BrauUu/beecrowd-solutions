local entry = io.read()
local t = {}
for value in string.gmatch(entry, '[^%s]+') do
    table.insert(t, value)
end
local departureTime = tonumber(t[1])
local travelTime = tonumber(t[2])
local arrivalTime = tonumber(t[3])

local newTime = departureTime + travelTime + arrivalTime
if newTime >= 24 then
    newTime = newTime - 24
elseif newTime < 0 then
    newTime = 24 + newTime
end
print(newTime)