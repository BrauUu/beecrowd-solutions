local i = 1
local j = 60

while j >= 0 do
    print(string.format('I=%i J=%i',i,j))
    i = i + 3
    j = j - 5
end