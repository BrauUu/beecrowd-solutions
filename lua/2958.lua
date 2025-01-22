local entry = io.read()
local temp = {}
for v in string.gmatch(entry, '%S+') do
    table.insert(temp, tonumber(v))
end

local t = {}

for i=1, temp[1] do
    entry = io.read()
    for v in string.gmatch(entry, '%S+') do
        table.insert(t, v)
    end
end

table.sort(t, function (a, b)
    if string.sub(a,2,2) == 'V' and string.sub(b,2,2)  == 'D' then
        return true
    elseif string.sub(a,2,2)  == 'D' and string.sub(b,2,2)  == 'V' then
        return false
    else
        if tonumber(string.sub(a,1,1)) > tonumber(string.sub(b,1,1)) then
            return true
        else
            return false
        end
    end
end)

for ind, v in ipairs(t) do
    print(v)
end