local n = io.read('n')
 
for i = 0, 9, 1 do
    print(string.format("N[%i] = %i", i, n))
    n = n * 2
end