local startDay = io.read()
local startTime = io.read()

local tempTable = {}
startDay = string.match(startDay, '%d+')
for n in string.gmatch(startTime, '%d+') do
    table.insert(tempTable, n)
end

local startHour = tonumber(tempTable[1])
local startMinute = tonumber(tempTable[2])
local startSecond = tonumber(tempTable[3])

tempTable = {}

local endDay = io.read()
local endTime = io.read()

endDay = string.match(endDay, '%d+')
for n in string.gmatch(endTime, '%d+') do
    table.insert(tempTable, n)
end

local endHour = tonumber(tempTable[1])
local endMinute = tonumber(tempTable[2])
local endSecond = tonumber(tempTable[3])

local days = endDay - startDay
local hours = endHour - startHour
local minutes = endMinute - startMinute
local seconds = endSecond - startSecond

if seconds < 0 then
    seconds = 60 + seconds
    minutes = minutes - 1
end
if minutes < 0 then
    minutes = 60 + minutes
    hours = hours - 1
end
if hours < 0 then
    hours = 24 + hours
    days = days - 1
end

print(days.." dia(s)")
print(hours.." hora(s)")
print(minutes.." minuto(s)")
print(seconds.." segundo(s)")