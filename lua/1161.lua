local function fatorialSum(n)
    local sumTable = {
        [0] = 1
    }
    local sum = 1
    for i = 1, n, 1 do
        sum = sum * i
        table.insert(sumTable, sum)
    end
    return sumTable
end

local sumTable = fatorialSum(20)

local function main()
    local entry = io.read()
    local t = {}
    for v in string.gmatch(entry, '[^%s]+') do
        table.insert(t, tonumber(v))
    end
    print(sumTable[t[1]] + sumTable[t[2]])
end


while true do
    -- for _, item in pairs(sumTable) do
    --     print(item)
    -- end
   if not pcall(main) then
        break
   end
end

