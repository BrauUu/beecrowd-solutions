local n = io.read('n')

for i = 1, n, 1 do
    local x = io.read('n')
    local s
    if x == 0 then
        s = 'NULL'
    elseif x % 2 == 0 then
        s = 'EVEN '
    else
        s = 'ODD '
    end

    if x < 0 then
        s = s..'NEGATIVE'
    elseif x > 0 then
        s = s..'POSITIVE'
    end

    print(s)
end