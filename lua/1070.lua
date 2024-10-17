local x = io.read('n')
local count = 0
local i = x
while count < 6 do
    if i % 2 == 1 then
        print(i)
        count = count + 1
    end
    i = i + 1
end