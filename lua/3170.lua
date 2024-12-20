local b = tonumber(io.read())
local g = tonumber(io.read())

local half = g//2

if b >= half then
    print('Amelia tem todas bolinhas!')
else
    print(string.format('Faltam %i bolinha(s)', half - b))
end