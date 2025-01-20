local t = tonumber(io.read())

for i=1, 1000 do
    print(string.format('N[%i] = %i', i-1, (i-1)%t))
end