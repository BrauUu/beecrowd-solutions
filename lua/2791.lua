local entry = io.read()
local i = 1
for v in string.gmatch(entry, '%S+') do
    if tonumber(v) == 1 then
        print(i)
        break
    end
    i = i + 1
end