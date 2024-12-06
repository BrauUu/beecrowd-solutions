local entry = io.read()
local temp = {}

for v in entry:gmatch('%S+') do
    table.insert(temp, tonumber(v))
end

local playersNum = temp[1]

entry = io.read()
temp = {}

for v in entry:gmatch('%S+') do
    table.insert(temp, tonumber(v))
end

local victoryPoints = {}
local winner
local winnerPoints = 0

for key, value in pairs(temp) do
    local rest = key % playersNum
    if rest == 0 then
        rest = playersNum
    end
    victoryPoints[rest] = (victoryPoints[rest] or 0) + value
    if victoryPoints[rest] >= winnerPoints then
        winner = rest
        winnerPoints = victoryPoints[rest]
    end
end

print(winner)
