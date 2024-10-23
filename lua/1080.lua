local pos
local biggest = 0

for i = 1, 100, 1 do
    local value = io.read("n")
    if value > biggest then
        biggest = value
        pos = i
    end
end

print(biggest)
print(pos)