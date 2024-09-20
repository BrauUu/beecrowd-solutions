local v = io.read('n')

if v >= 0 and v <= 25 then
    print("Intervalo [0,25]")
elseif v > 25 and v <= 50 then
    print("Intervalo (25,50]")
elseif v > 50 and v <= 75 then
    print("Intervalo (50,75]")
elseif v > 75 and v <= 100 then
    print("Intervalo (75,100]")
else
    print('Fora de intervalo')
end