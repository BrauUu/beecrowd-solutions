local time = io.read('n')
local speed = io.read('n')

local distance = time * speed
local litters = distance / 12

print(string.format("%.3f", litters))