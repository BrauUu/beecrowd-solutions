local entry = io.read()
local t = {}
for v in string.gmatch(entry, '[^%s]+') do
    table.insert(t, tonumber(v))
end

local initialHour = t[1]
local initialMinute = t[2]
local finalHour = t[3]
local finalMinute = t[4]

local totalInitialMinutes = initialHour * 60 + initialMinute
local totalFinalMinutes = finalHour * 60 + finalMinute

local minutesDiff = totalFinalMinutes - totalInitialMinutes
if minutesDiff <= 0 then
    minutesDiff = 1440 + minutesDiff
end

print('O JOGO DUROU '..string.format('%i', minutesDiff // 60)..' HORA(S) E '..string.format('%i', minutesDiff % 60)..' MINUTO(S)')