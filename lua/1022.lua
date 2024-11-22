local function mdc(a, b)
    local aCopy = a
    local bCopy = b
    while b ~= 0 do
        local resto = a % b
        a = b
        b = resto
    end
    return string.format('%i/%i', aCopy / a, bCopy/ a)
end

local n = tonumber(io.read())

for i=1, n do
    local entry = io.read()
    local temp = {}
    for value in string.gmatch(entry, "[^%s/]+") do
        table.insert(temp, value)
    end
    local operator = '/'
    if #temp == 5 then
        operator = table.remove(temp, 3)
    end
    local n1 = tonumber(temp[1])
    local d1 = tonumber(temp[2])
    local n2 = tonumber(temp[3])
    local d2 = tonumber(temp[4])
    
    local operations = {
        ["+"] = tostring(n1*d2 + n2*d1).."/"..tostring(d1*d2),
        ["-"] = tostring(n1*d2 - n2*d1).."/"..tostring(d1*d2),
        ["*"] = tostring(n1 * n2).."/"..tostring(d1*d2),
        ["/"] = string.format("%i/%i", n1*d2, n2*d1)
    }

    local response = operations[operator]
    temp = {}
    for value in string.gmatch(response, "[^/]+") do
        table.insert(temp, tonumber(value))
    end
    print(string.format("%s = %s", response, mdc(temp[1], temp[2])))
end