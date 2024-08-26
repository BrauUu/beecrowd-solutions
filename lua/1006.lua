local a = io.read("n")
local b = io.read("n")
local c = io.read("n")

local avg = ((a*2)+(b*3)+(c*5))/10

print("MEDIA = "..string.format("%.1f", avg))