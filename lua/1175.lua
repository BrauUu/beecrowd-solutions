local vector = {}
for i=1, 20 do
    local v = tonumber(io.read())
    table.insert(vector, v)
end

local j = 20
for i=1, 10 do
    local temp = vector[j]
    vector[j] = vector[i]
    vector[i] = temp
    j = j - 1
end

for k, v in pairs(vector) do
    print(string.format('N[%i] = %i', k-1, v))
end