local n = tonumber(io.read())

local res = ''

for i=0, n-1 do
    res = res..'Ho '
end

print(string.sub(res, 1, #res-1)..'!')