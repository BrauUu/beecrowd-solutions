local conector1 = io.read()
local conector2 = io.read()
local flag = false
for i=1,10,2 do
    if tonumber(string.sub(conector1, i, i)) == tonumber(string.sub(conector2, i, i)) then
        flag = true
        break
    end
end

if flag then
    print('Y')
else
    print('N')
end