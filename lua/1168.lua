local leds = {
    [1] = 2,
    [2] = 5,
    [3] = 5,
    [4] = 4,
    [5] = 5,
    [6] = 6,
    [7] = 3,
    [8] = 7,
    [9] = 6,
    [0] = 6
}

local n = tonumber(io.read())

for i=1, n do
    local v = io.read()
    local sum = 0
    for num in string.gmatch(v, ".") do
        sum = sum + leds[tonumber(num)]
    end
    print(string.format('%i leds', sum))
end