local entry = io.read()
local sum = 0
for v in string.gmatch(entry, '%S+') do
    sum = sum + tonumber(v)
end

print(sum - 3)