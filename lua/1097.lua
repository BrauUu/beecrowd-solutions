local j = 7
for i=1, 9, 2 do
    for g=0,2,1 do
        print(string.format('I=%i J=%i', i, j-g))
    end
    j = j + 2
end