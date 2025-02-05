local n = tonumber(io.read())

for i=n, 1, -1 do
    if n % i == 0 then
        print(n//i)
    end
end