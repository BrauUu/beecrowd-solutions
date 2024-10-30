local continue = 1
while continue == 1 do
    local count = 0
    local sum = 0
    while count < 2 do
        local n = io.read("n")
        if n >= 0 and n <= 10 then
            count = count + 1
            sum = sum + n
        else
            print('nota invalida')
        end
    end
    print(string.format("media = %.2f", sum / 2))
    repeat
        print("novo calculo (1-sim 2-nao)")
        continue = io.read('n')
    until continue == 1 or continue == 2
end