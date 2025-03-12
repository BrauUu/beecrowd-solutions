local t = {1}
for i=2, 40 do
    table.insert(t, i, ((t[i-1] or 1) + (t[i-2] or 1)))
end

while true do
    local n = tonumber(io.read())
    if n == 0 then
        break
    end
    print(t[n])
end