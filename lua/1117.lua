local sum = 0
local count = 0

while count < 2 do
    local grade = tonumber(io.read())
    if grade >= 0 and grade <= 10 then
        count = count + 1
        sum = sum + grade
    else
        print("nota invalida")
    end
    if count == 2 then
        print(string.format('media = %.2f', sum / 2))
    end
end