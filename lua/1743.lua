local conector1 = io.read()
local conector2 = io.read()
local notCompatible = false
for i=1,9,2 do
    if tonumber(string.sub(conector1, i, i)) == tonumber(string.sub(conector2, i, i)) then
        notCompatible = true
        break
    end
end

if notCompatible then
    print('N')
else
    print('Y')
end