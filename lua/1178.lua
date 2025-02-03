local n = tonumber(io.read())

for i=0, 99 do
    print(string.format('N[%i] = %.4f', i, n))
    n = n / 2
end