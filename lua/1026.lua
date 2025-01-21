local function decToBin(x)
    local bin = ''
    local dec = x
    while dec ~= 0 do
        local rest = dec % 2
        dec = dec // 2
        bin = tostring(rest) .. bin
    end
    return bin
end

local function binSum(x, y)
    local len
    local sum = ''
    local carry = false
    if #x > #y then
        len = #x
    else
        len = #y
    end
    for i = 0, len - 1 do
        local v1 = 0
        local v2 = 0
        if #x - i > 0 and #string.sub(x, #x - i, #x - i) > 0 then
            v1 = tonumber(string.sub(x, #x - i, #x - i))
        end
        if #y - i > 0 and #string.sub(y, #y - i, #y - i) > 0 then
            v2 = tonumber(string.sub(y, #y - i, #y - i))
        end
        local tempSum = v1 + v2
        if carry then
            tempSum = tempSum + 1
        end
        if tempSum == 0 or tempSum == 1 then
            sum = tostring(tempSum) .. sum
            carry = false
        elseif tempSum == 2 then
            sum = '0' .. sum
            carry = true
        else
            sum = '1' .. sum
            carry = true
        end
    end
    if carry then
        sum = '1' .. sum
    end
    return sum
end

local function binSumMofiz(x, y)
    local len
    local sum = ''
    if #x > #y then
        len = #x
    else
        len = #y
    end
    for i = 0, len - 1 do
        local v1 = 0
        local v2 = 0
        if #x - i > 0 and #string.sub(x, #x - i, #x - i) > 0 then
            v1 = tonumber(string.sub(x, #x - i, #x - i))
        end
        if #y - i > 0 and #string.sub(y, #y - i, #y - i) > 0 then
            v2 = tonumber(string.sub(y, #y - i, #y - i))
        end
        local tempSum = v1 + v2
        if tempSum == 0 or tempSum == 1 then
            sum = tostring(tempSum) .. sum
        end
    end
    return sum
end

local function binToDec(x)
    local dec = 0
    local bin = x
    for i = 0, #bin - 1 do
        dec = dec + (tonumber(string.sub(bin, #bin - i, #bin - i)) * (2 ^ i))
    end
    return dec
end

local function main()
    local entry = io.read()
    local t = {}
    for value in string.gmatch(entry, "%S+") do
        table.insert(t, value)
    end
    local x = t[1]
    local y = t[2]
    local bin1 = decToBin(x)
    local bin2 = decToBin(y)
    local binSumRes = binSumMofiz(bin1, bin2)
    print(string.format('%i', binToDec(binSumRes)))
end

while true do
    if not pcall(main) then
        break
    end
end
