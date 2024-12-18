local n = tonumber(io.read())
local count = 0

for i=1, n do
    local carDoor = tonumber(io.read())
    if carDoor ~= 1 then
        count = count + 1
    end
end

print(count)