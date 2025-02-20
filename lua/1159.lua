while true do
    local x = tonumber(io.read())
    if x == 0 then
        break
    end
    local sum = 0
    for i=x, x+9 do
        if i % 2 == 0 then
            sum = sum + i
        end
    end
    print(sum)
end