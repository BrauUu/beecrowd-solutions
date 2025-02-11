local odds = {}
local evens = {}

for i=1, 15 do
    local x = tonumber(io.read())
    if x % 2 == 0 then
        table.insert(odds, x)
        if #odds == 5 then
            for ind, v in ipairs(odds) do
                print(string.format('par[%i] = %i', ind - 1, v))
            end
            odds = {}
        end
    else
        table.insert(evens, x)
        if #evens == 5 then
            for ind, v in ipairs(evens) do
                print(string.format('impar[%i] = %i', ind - 1, v))
            end
            evens = {}
        end
    end
end

for ind, v in ipairs(evens) do
    print(string.format('impar[%i] = %i', ind - 1, v))
end

for ind, v in ipairs(odds) do
    print(string.format('par[%i] = %i', ind - 1, v))
end
