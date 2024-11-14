local x = io.read('n')
for j = 1, x do
    local n = io.read('n')
    local flag = false
    local nSqrt = tonumber(math.sqrt(n))
    for i = 2, nSqrt do
        if n % i == 0 then
            print('Not Prime')
            flag = true
            break
        end
    end
    if not flag then
        print('Prime')
    end
end