local n = io.read("n")
local i = 0
while true do
    local v = (n * i) + 2
    if v > 10000 then
        break
    end
    print(v)
    i = i + 1
end