local function main()
    local entry = io.read()
    local t = {}
    for value in string.gmatch(entry, "%S+") do
        table.insert(t, tonumber(value))
    end
    local A = t[1]
    local B = t[2]
    local C = t[3]
    if A ~= B and A ~= C then
        print('A')
    elseif B ~= A and B ~= C then
        print('B')
    elseif C ~= A and C ~= B then
        print('C')
    else
        print('*')
    end
end

while true do
    if not pcall(main) then
        break
    end
end
