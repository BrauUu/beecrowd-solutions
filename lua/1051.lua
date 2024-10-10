local salary = io.read('n')
local tax = 0

if salary <= 2000 then
    print("Isento")
    return
end

if salary > 2000 then
    local value = salary - 2000
    if value > 1000 then
        value = 1000
    end
    local percent = 8
    tax = tax + value / 100 * percent
end
if salary > 3000 then
    local value = salary - 3000
    if value > 1500 then
        value = 1500
    end
    local percent = 18
    tax = tax + value / 100 * percent
end
if salary > 4500 then
    local value = salary - 4500
    local percent = 28
    tax = tax + value / 100 * percent
end

print(string.format("R$ %.2f", tax))