local n = tonumber(io.read())

for i=1, n do
    local entry = io.read()
    local shoppingList = {}
    for word in string.gmatch(entry, '%S+') do
        local flag = false
        for k, item in pairs(shoppingList) do
            if word == item then
                flag = true
            end
        end
        if not flag then
            table.insert(shoppingList, word)
        end
    end
    table.sort(shoppingList)
    local res = ''
    for k, item in pairs(shoppingList) do
        res = res..item..' '
    end
    print(string.sub(res, 1, #res - 1))
end