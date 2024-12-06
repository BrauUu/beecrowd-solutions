local entry = io.read()
local temp = {}

for v in entry:gmatch('%S+') do
    table.insert(temp, tonumber(v))
end

print(string.format("%.2f", temp[1] / (temp[2] + temp[3])))