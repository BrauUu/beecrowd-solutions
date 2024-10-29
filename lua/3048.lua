local n = io.read("n")
local last = -1
local count = 0
for _ = 1, n, 1 do
    local v = io.read("n")
    if v ~= last then
        count = count + 1
    end
    last = v
end
print(count)