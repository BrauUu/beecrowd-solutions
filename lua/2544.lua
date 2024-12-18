local function main()
    local n = tonumber(io.read())
    local count = 0
    local v = 2
    while v <= n do
        count = count + 1
        v = v * 2
    end
    print(count)
end

while true do
    if not pcall(main) then
        break
    end
end