local n = tonumber(io.read())
local nets = {}
local area = 0

for i = 1, n do
    local entry = io.read()
    local temp = {}
    for v in string.gmatch(entry, "%S+") do
        table.insert(temp, tonumber(v))
    end
    local xi = temp[1]
    local xf = temp[2]
    local yi = temp[3]
    local yf = temp[4]
    local net = {
        ['xi'] = xi,
        ['xf'] = xf,
        ['yi'] = yi,
        ['yf'] = yf,
    }
    table.insert(nets, net)
end

for i = 1, 100 do
    for j = 1, 100 do
        for k = 1, n do
            if nets[k]['xi'] <= i and nets[k]['xf'] > i and nets[k]['yi'] <= j and nets[k]['yf'] > j then
                area = area + 1
                break
            end
        end
    end
end

print(area)