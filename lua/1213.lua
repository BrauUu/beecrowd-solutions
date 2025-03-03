local function main()
    local num = tonumber(io.read())
    local count = 0
    local i = 1
    while i % num ~= 0 do
        local n = (10 * i + 1)
        i = n % num
        count = count + 1
        print(i)
    end
    print(count + 1)
end

while true do
    if not pcall(main) then
        break
    end
end