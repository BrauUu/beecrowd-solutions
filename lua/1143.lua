local n = tonumber(io.read())

for i=1, n do
    print(string.format('%i %i %i', i, i^2, i^3))
end