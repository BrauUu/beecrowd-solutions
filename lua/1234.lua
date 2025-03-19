local function main()
    local x = io.read()
    local newX = ''
    local capital = true
    for i = 1, #x do
        local char = string.sub(x, i, i)
        if char ~= ' ' then
            if capital then
                char = string.upper(char)
            else
                char = string.lower(char)
            end
            capital = not capital
        end
        newX = newX..char
    end
    print(newX)
end

while true do
    if not pcall(main) then
        break
    end
end