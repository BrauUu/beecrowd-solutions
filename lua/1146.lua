while true do
    local x = tonumber(io.read())
    local res = ''
    if x == 0 then
        break
    end
    for i=1, x do
        res = res..tostring(i)..' '
    end
    print(string.sub(res, 1, #res-1))
end