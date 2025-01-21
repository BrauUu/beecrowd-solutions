local n = tonumber(io.read())

local j = 1
for i=1, n do
    print(string.format('%i %i %i PUM',j, j+1, j+2))
    j = j + 4
end