local function main()
    local entry = io.read()
    local temp = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(temp, tonumber(v))
    end
    local n = temp[1]
    local r = temp[2]

    entry = io.read()
    local tempString = ''
    for i=1, n do
        tempString = tempString..tostring(i)..' '
    end
    tempString = string.sub(tempString, 0, #tempString - 1)
    for v in string.gmatch(entry, '%S+') do
        pcall(function ()
            local startIndex, endIndex = string.find(tempString, tostring(v))
            tempString = string.sub(tempString, 0, startIndex-1)..string.sub(tempString, endIndex+1, #tempString)
        end)
    end
    local res = ''
    for v in string.gmatch(tempString, '%S+') do
        res = res..v..' '
    end
    if #res > 1 then
        print(res)
    else
        print('*')
    end
end

while true do
    if not pcall(main) then
        break
    end
end