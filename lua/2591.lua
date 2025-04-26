local n = tonumber(io.read())

for _ = 1, n do
    local c = io.read()
    local ind = c:find('m')
    local x = #c:sub(2, ind - 1)
    ind = c:find('m',ind+1)
    local y = #c:sub(5+x, ind - 1)
    print('k'..('a'):rep(x*y))
end