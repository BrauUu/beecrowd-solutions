local entry = io.read()
local t = {}
for v in string.gmatch(entry, '[^%s]+') do
    table.insert(t, tonumber(v))
end

local startTime = t[1]
local endTime = t[2]

local time = 0

if startTime >= endTime then
    time = 24 - startTime + endTime
else
    time = endTime - startTime
end

print('O JOGO DUROU '..time..' HORA(S)')