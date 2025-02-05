local sum = 0
local count = 0
while true do
    local x = tonumber(io.read())
    if x < 0 then
        break
    end
    sum = sum + x
    count = count + 1
end

print(string.format('%.2f', sum / count))