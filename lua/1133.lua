local function getSmallerBetweenTwoNumbers(n1, n2)
    if n1 < n2 then
        return n1
    else
        return n2
    end
end

local function getBiggerBetweenTwoNumbers(n1, n2)
    if n1 > n2 then
        return n1
    else
        return n2
    end
end

local n1 = io.read('n')
local n2 = io.read('n')

local sm = getSmallerBetweenTwoNumbers(n1, n2)
local bg = getBiggerBetweenTwoNumbers(n1, n2)

for i = sm + 1, bg - 1, 1 do
    if i % 5 == 2 or i % 5 == 3 then
        print(i)
    end
end