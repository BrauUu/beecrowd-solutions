local name = io.read()
local salary = io.read("n")
local totalSellings = io.read("n")

local total = salary + (15*totalSellings/100)

print("TOTAL = R$ "..string.format("%.2f",total))