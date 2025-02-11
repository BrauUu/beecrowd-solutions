local entry = io.read()
local temp = {}

for v in string.gmatch(entry, '%S+') do
    table.insert(temp, tonumber(v))
end

local x = temp[1]
local y = temp[2]

local res = ''

for i=1, y do
    res = res..tostring(i)..' '
    if i % x == 0 then
        print(string.sub(res, 1, #res - 1))
        res = ''
    end
end

if res ~= '' then
    print(string.sub(res, 1, #res - 1))
end