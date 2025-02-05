local x = tonumber(io.read())
local y = tonumber(io.read())

local sum = 0
local smlst
local bgst

if x > y then
    smlst = y
    bgst = x
else
    smlst = x
    bgst=y
end

for i=smlst, bgst, 1 do
    if i % 13 ~= 0 then
        sum = sum + i
    end
end

print(sum)