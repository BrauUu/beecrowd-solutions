while true do
    local n = io.read('n')
    if n == 0 then
        break
    end
    local stack = {}
    for i=1, n do
        table.insert(stack, i)
    end
    local discardedCards = {}
    while #stack > 1 do
        local discardedCard = table.remove(stack, 1)
        table.insert(discardedCards, discardedCard)
        local temp = table.remove(stack, 1)
        table.insert(stack, #stack + 1, temp)
    end
    local text = 'Discarded cards:'
    for ind, card in ipairs(discardedCards) do
        if ind > 1 then
            text = text..string.format(', %i', card)
        else
            text = text..string.format(' %i', card)
        end
    end
    print(text)
    print('Remaining card: '..tostring(stack[1]))
end