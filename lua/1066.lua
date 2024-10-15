local evenCount = 0
local oddCount = 0
local positiveCount = 0
local negativeCount = 0

for i = 1, 5, 1 do
    local n = io.read("n")
    if n % 2 == 0 then
        evenCount = evenCount + 1
    else
        oddCount = oddCount + 1
    end

    if n > 0 then
        positiveCount = positiveCount + 1
    elseif n < 0 then
        negativeCount = negativeCount + 1
    end
end

print(evenCount.." valor(es) par(es)")
print(oddCount.." valor(es) impar(es)")
print(positiveCount.." valor(es) positivo(s)")
print(negativeCount.." valor(es) negativo(s)")