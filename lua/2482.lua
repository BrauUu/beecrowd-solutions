local n = tonumber(io.read())
local translations = {}

for _ = 1, n do
    local language = io.read()
    local greetings = io.read()
    translations[language] = greetings
end

local m = tonumber(io.read())

for _ = 1, m do
    local name = io.read()
    local language = io.read()
    print(name)
    print(translations[language].."\n")
end