local evenCount = 0

for i = 1, 5, 1 do
    local num = io.read("n")
    if num % 2 == 0 then
        evenCount = evenCount + 1
    end
end

print(evenCount.." valores pares")