local n = tonumber(io.read())
local total = 0
local cTotal = 0
local rTotal = 0
local sTotal = 0
for i=1,n do
    local entry = io.read()
    local t = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(t, v)
    end
    local num = tonumber(t[1])
    local type = t[2]
    if type == 'C' then
        cTotal = cTotal + num
    elseif type == 'R' then
        rTotal = rTotal + num
    elseif type == 'S' then
        sTotal = sTotal + num
    end
    total = total + num
end

print(string.format('Total: %i cobaias', total))

print(string.format('Total de coelhos: %i', cTotal))
print(string.format('Total de ratos: %i', rTotal))
print(string.format('Total de sapos: %i', sTotal))

print(string.format('Percentual de coelhos: %.2f ' , cTotal * 100 / total)..'%')
print(string.format('Percentual de ratos: %.2f ', rTotal * 100 / total)..'%')
print(string.format('Percentual de sapos: %.2f ', sTotal * 100 / total)..'%')