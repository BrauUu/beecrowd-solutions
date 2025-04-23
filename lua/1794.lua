local n = tonumber(io.read())

local entry = io.read()
local t = {}

for v in string.gmatch(entry, '%S+') do
    table.insert(t, tonumber(v))
end

local la = t[1]
local lb = t[2]
entry = io.read()
t = {}

for v in string.gmatch(entry, '%S+') do
    table.insert(t, tonumber(v))
end

local sa = t[1]
local sb = t[2]

if n >= la and n <= lb and n >= sa and n <= sb then
    print('possivel')
else
    print('impossivel')
end