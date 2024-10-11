local count = 0
for i = 1, 6, 1 do
    local num = io.read('n')
    if num > 0 then
        count = count + 1
    end
end
print(string.format("%i valores positivos", count))