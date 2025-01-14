local function factorial(n)
    if n == 1 then
        return n
    end
    return n * factorial(n-1)
end

local n = tonumber(io.read())
print(factorial(n))