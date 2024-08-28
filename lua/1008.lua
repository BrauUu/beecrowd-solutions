local number = io.read("n")
local hours = io.read("n")
local salaryPerHour = io.read("n")

local salary = salaryPerHour * hours

print("NUMBER = "..number)
print("SALARY = U$ "..string.format("%.2f", salary))