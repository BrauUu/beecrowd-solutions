local res = ''
for i=0, 99 do
    local n = tonumber(io.read())
    if n <= 10 then
        res = res..string.format('A[%i] = %.1f', i, n)..'\n'
    end
end
print(string.sub(res, 1, #res - 1))