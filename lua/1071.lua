local x = io.read('n')
local y = io.read('n')

local sm
local lg

if x > y then
    sm = y
    lg = x
else
    sm = x
    lg = y
end

local sum = 0
local i = sm + 1
while i < lg do
    if i % 2 == 1 then
        sum = sum + i
    end
    i = i + 1
end
print(sum)