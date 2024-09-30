local originalSalary = io.read('n')
local newSalary
local percent
local addition

if originalSalary <= 400 then
    percent = 15
elseif originalSalary <= 800 then
    percent = 12
elseif originalSalary <= 1200 then
    percent = 10
elseif originalSalary <= 2000 then
    percent = 7
else
    percent = 4
end

addition = originalSalary / 100 * percent
newSalary = originalSalary + addition

print('Novo salario: '..string.format('%.2f', newSalary))
print('Reajuste ganho: '..string.format('%.2f', addition))
print('Em percentual: '..percent..' %')