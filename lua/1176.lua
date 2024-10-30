local function fibonacci()
    local t = {
        [0] = 0,
        [1] = 1
    }
    for i = 2, 60, 1 do
        local n = t[i-1] + t[i-2]
        t[i] = n
    end
    return t
end

local fib = fibonacci()

local t = io.read('n')
for _ = 0, t-1, 1 do
    local n = io.read('n')
    print(string.format("Fib(%i) = %i",n, fib[n]))
end
