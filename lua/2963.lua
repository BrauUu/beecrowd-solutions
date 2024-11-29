local n = tonumber(io.read())
local winnerVotes = 0
local winnerId = 0
for i=1, n do
    local votes = tonumber(io.read())
    if votes > winnerVotes then
        winnerVotes = votes
        winnerId = i
    end
end

if winnerId == 1 then
    print('S')
else
    print('N')
end