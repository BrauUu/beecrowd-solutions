local entry = io.read()
local t = {}

for v in string.gmatch(entry, '[^%s]+') do
    table.insert(t, v)
end

if t[2] % t[1] == 0 or t[1] % t[2] == 0 then
    print('Sao Multiplos')
else
    print('Nao sao Multiplos')
end