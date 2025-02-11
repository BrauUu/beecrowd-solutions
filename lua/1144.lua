local n = tonumber(io.read())

for i=1, n do
    print(string.format('%i %i %i', i, i^2, i^3))
    print(string.format('%i %i %i', i, i^2 + 1, i^3 + 1))
end