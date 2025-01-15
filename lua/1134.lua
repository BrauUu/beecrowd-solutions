local counts = {
    ['Alcool'] = 0,
    ['Gasolina'] = 0,
    ['Diesel'] = 0,

}

local codes = {
    [1] = 'Alcool',
    [2] = 'Gasolina',
    [3] = 'Diesel'

}
while true do
    local cod = tonumber(io.read())
    if cod == 4 then
        break
    end
    if codes[cod] then
        local key = codes[cod]
        local value = counts[key]
        counts[key] = value + 1
    end
end

print('MUITO OBRIGADO')

for ind, key  in ipairs(codes) do
    print(string.format('%s: %i',key, counts[key]))
end