local positivesCount = 0
local sum = 0
for i = 1, 6, 1 do
    local num = io.read('n')
    if num > 0 then
        positivesCount = positivesCount + 1
        sum = sum + num
    end
end

print(positivesCount.." valores positivos")
print(string.format('%.1f', sum / positivesCount))