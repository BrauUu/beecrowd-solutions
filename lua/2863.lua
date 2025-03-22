local function main()
    local t = tonumber(io.read())
    local bestTime = 12
    for _ = 1, t do
        local time = tonumber(io.read())
        if time < bestTime then
            bestTime = time
        end
    end
    print(string.format('%.2f', bestTime))
end

while true do
    if not pcall(main) then
        break
    end
end
