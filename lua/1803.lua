local function getNum(index, t)
    local res = ''
    for i = 1, 4 do
        res = res..t[i][index]
    end
    return tonumber(res)
end

local t = {
    {},
    {},
    {},
    {}
}

for i = 1, 4 do
    local entry = io.read()
    for v in string.gmatch(entry, '.') do
        table.insert(t[i], v)
    end
end

local f = getNum(1, t)
local l = getNum(#t[1], t)
local res = ''

for i = 2 , #t[1]-1 do
    local m = getNum(i, t)
    local charCode = (f*m+l) % 257
    res = res..string.char(charCode)
end

print(res)