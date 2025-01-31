local n = tonumber(io.read())

local x = 1
local fat = 1
local maxX = 0
local maxFat = 0

while fat < n do
    maxFat = fat
    maxX = x
    x = x + 1
    fat = fat * x
end

local count = 1
x = maxX
fat = maxFat
n = n - fat

while n ~= 0 do
    if fat > n then
        fat = fat // x
        x = x - 1
    else
        n = n - fat
        count = count + 1
    end
end

print(count)