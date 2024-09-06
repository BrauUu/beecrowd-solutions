local days = io.read("n")

local years = days // 365
days = days - years * 365
local months = days // 30
days = days - months * 30

print(years.." ano(s)")
print(months.." mes(es)")
print(days.." dia(s)")