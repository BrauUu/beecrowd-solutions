local n = tonumber(io.read())

for i=1, n do
    local entry = io.read()
    local t = {}
    for v in string.gmatch(entry ,"[^%s]+") do
        table.insert(t, tonumber(v))
    end
    local n1 = t[1]
    local n2 = t[2]
    
    local mdc = 0
    local bgst
    local smlst

    if n1 < n2 then
        smlst = n1
        bgst = n2
    else
        smlst = n2
        bgst = n1
    end

    while true do
        local rest = bgst % smlst
        if rest == 0 then
            break
        end
        bgst = smlst
        smlst = rest
    end
    print(smlst)
end