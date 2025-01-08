local n = tonumber(io.read())
local entry = io.read()
local i = 0
local ind = 0
local smallest = 0
for v in string.gmatch(entry, '%S+') do
    local value = tonumber(v)
    if i == 0 then
        smallest = value
    end
    if value < smallest then
        smallest = value
        ind = i
    end
    i = i + 1
end

print('Menor valor: '..smallest)
print('Posicao: '..ind)