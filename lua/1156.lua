local s = 1

local x = 3
local y = 2

while x <= 39 do
    s = s + (x/y)
    x = x + 2
    y = y * 2
end

print(string.format('%.2f', s))