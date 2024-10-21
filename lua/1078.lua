local n = io.read("n")

for i = 1, 10,1 do
    print(string.format("%i x %i = %i", i, n, i*n))
end