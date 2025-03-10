while true do
    local n = tonumber(io.read())
    if n == 0 then
        break
    end
    local biggest = n
    while n ~= 1 do
        if n % 2 == 0 then
            n = math.floor(1/2 * n)
        else
            n = 3 * n + 1
        end
        if n > biggest then
            biggest = n
        end
    end
    print(biggest)
end