local function fn()
    local t = {}
    for i=1, 100 do
        table.insert(t, i, (i*i + (t[i-1] or 0)))
    end
    return t
end

local t = fn()

while true do
    local n = tonumber(io.read())
    if n == 0 then
        break
    end
    print(t[n])
end