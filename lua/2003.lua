local function main()
    local time = io.read()
    local hour = tonumber(time:sub(1,1))
    local minutes = tonumber(time:sub(3,4))
    minutes = (minutes + 60) % 60
    hour = hour + 1
    local delay = 0
    if hour >= 8 then
        delay = (hour - 8) * 60 + minutes
    end
    print('Atraso maximo: '..tostring(delay))
end

while true do
    if not pcall(main) then
        break
    end
end