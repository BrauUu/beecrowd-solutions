local entry = io.read()
local bgst = 0
for v in string.gmatch(entry, '%S+') do
    local n = tonumber(v)
    if n > bgst then
        bgst = n
    end
end

print(bgst)