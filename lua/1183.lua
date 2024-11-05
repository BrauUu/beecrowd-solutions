local operation = io.read()
local sum = 0
local count = 0
for i = 0, 11, 1 do
    for g = 0, 11, 1 do
        local n = io.read('n')
        if g > i then
            sum = sum + n
            count = count + 1
        end
    end
end

if operation == 'S' then
    print(string.format('%.1f', sum))
elseif operation == 'M' then
    print(string.format('%.1f', sum / count))
end