local n = tonumber(io.read())

for _=1, n do
    local x = tonumber(io.read())
    local flag = true
    if x > 2 then
        for i=2, x//2, 1 do
            if x % i == 0 then
                flag = false
                break
            end
        end
    end
    if flag then
        print(string.format('%i eh primo', x))
    else
        print(string.format('%i nao eh primo', x))
    end
end