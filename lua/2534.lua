local function main()
    local entry = io.read()
    local temp = {}
    for v in string.gmatch(entry, '%S+') do
        table.insert(temp, tonumber(v))
    end
    local n = temp[1]
    local q = temp[2]

    local grades = {}

    for i = 1, n do
        local grade = tonumber(io.read())
        table.insert(grades, grade)
    end

    table.sort(grades, function(a, b)
        return a > b
    end)

    for i = 1, q do
        local query = tonumber(io.read())
        print(grades[query])
    end
end

while true do
    if not pcall(main) then
        break
    end
end
