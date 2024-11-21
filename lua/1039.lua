-- from math import sqrt

-- while True:
--     try:
--         r1, x1, y1, r2, x2, y2 = map(int, input().split())
        
--         distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
--         print('RICO' if distance + r2 <= r1 else 'MORTO')
        
--     except:
--         break

local function main()
    local entry = io.read()
    local temp = {}
    for value in string.gmatch(entry, '[^%s]+') do
        table.insert(temp, tonumber(value))
    end
    local r1 = temp[1]
    local x1 = temp[2]
    local y1 = temp[3]
    local r2 = temp[4]
    local x2 = temp[5]
    local y2 = temp[6]

    local distance = math.sqrt((x1-x2)^2 + (y1-y2)^2)

    if distance + r2 <= r1 then
        print('RICO')
    else
        print('MORTO')
    end

end

while true do
    if not pcall(main) then
        break
    end
end