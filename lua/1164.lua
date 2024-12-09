local n = tonumber(io.read())

for i=1,n do
    local x = tonumber(io.read())
    local sum = 0
    for j=1, x/2 do
        if x % j == 0 then
            sum = sum + j
        end
    end
    if sum == x then
        print(string.format('%i eh perfeito', x))
    else
        print(string.format('%i nao eh perfeito', x))
    end
end