local function main()
    local entry = io.read()
    local temp = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(temp, tonumber(v))
    end
    print(temp[1]* temp[2] * 2)
end

while true do
    if not pcall(main) then
        break
    end
end
