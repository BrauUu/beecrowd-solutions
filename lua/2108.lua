local biggestWord = ''
while true do
    local phrase = io.read()
    if phrase == '0' then
        break
    end
    local newPhrase = ''
    for word in string.gmatch(phrase, '%S+') do
        newPhrase = newPhrase..tostring(#word)..'-'
        if #word >= #biggestWord then
            biggestWord = word
        end
    end

    print(string.sub(newPhrase, 1, #newPhrase - 1))
end

print('\nThe biggest word: '..biggestWord)