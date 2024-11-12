local function main()
    local expr = io.read()
    local openParenthesisCount = 0
    local closeParenthesisCount = 0
    for i = 0, #expr do
        local char = string.sub(expr, i, i)
        if char == '(' then
            openParenthesisCount = openParenthesisCount + 1
        elseif char == ')' then
            closeParenthesisCount = closeParenthesisCount + 1
            if openParenthesisCount > 0 then
                openParenthesisCount = openParenthesisCount - 1
                closeParenthesisCount = closeParenthesisCount - 1
            end
        end
    end
    if openParenthesisCount == 0 and closeParenthesisCount == 0 then
        print('correct')
        return
    end
    print('incorrect')
end

while true do
    if not pcall(main) then
         break
    end
 end