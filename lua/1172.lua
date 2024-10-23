local tb = {}
for i = 0, 9, 1 do
    local value = io.read('n')
    if value <= 0 then
        value = 1
    end
    tb[i] = value
end

for i = 0, 9, 1 do
    print(string.format("X[%i] = %i", i, tb[i]))
end