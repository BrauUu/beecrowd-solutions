local function main()
    local text = io.read()
    local newtext = ''
    local italic = false
    local bold = false
    for i=1, #text do
        local char = string.sub(text, i, i)
        if char == '_' then
            if italic == false then
                char = '<i>'
            else
                char = '</i>'
            end
            italic = not italic
        elseif char == '*' then
            if bold == false then
                char = '<b>'
            else
                char = '</b>'
            end
            bold = not bold
        end
        newtext = newtext..char
    end
    print(newtext)
end

while true do
    if not pcall(main) then
        break
    end
end