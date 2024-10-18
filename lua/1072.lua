local n = io.read('n')
local count = 0

for i = 1, n, 1 do
    local v = io.read('n')
    if v >= 10 and v <= 20 then
        count = count + 1
    end
end

print(count.." in")
print(n-count.." out")