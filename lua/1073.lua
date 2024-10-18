local n = io.read('n')

for i = 2, n, 2 do
    print(string.format('%i^%i = %i', i, 2, i^2))
end