local n = tonumber(io.read())

for i=1,n do
    local entry = io.read()
    local temp = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(temp, tonumber(v))
    end
    local pa = temp[1]
    local pb = temp[2]
    local ga = temp[3]
    local gb = temp[4]

    local count = 0
    while pa <= pb and count <= 100 do
        pa = pa + (pa * ga / 100)//1
        pb = pb + (pb * gb / 100)//1
        count = count + 1
    end
    if count > 100 then
        print('Mais de 1 seculo.')
    else
        print(string.format('%i anos.', count))
    end
end