while true do
    local entry = io.read()
    local t = {}
    
    for value in string.gmatch(entry, "[^%s]+") do
        table.insert(t, tonumber(value))
    end
    
    local n = t[1]
    local k = t[2]
    local m = t[3]

    if n == 0 and k == 0 and m == 0 then
        break
    end
    
    local l = {}
    for i=1, n do
        table.insert(l, i, i)
    end
    
    local kIndex = 1
    local mIndex = n
    local res = ''
    while #l > 0 do
    
        if kIndex > #l then
            kIndex = 1
        end
        kIndex = kIndex + (k-1)
        if kIndex > #l then
            kIndex = (kIndex % #l)
            if kIndex == 0 then
                kIndex = #l
            end
        end
        if mIndex < 1 then
            mIndex = #l
        end
        mIndex = mIndex - (m) + 1
        if mIndex < 1 then
            mIndex = mIndex % #l
            if mIndex == 0 then
                mIndex = #l
            end
        end
        res = res..string.format("%3d", l[kIndex])
    
        if kIndex ~= mIndex then
            res = res..string.format("%3d", l[mIndex])
            table.remove(l, mIndex)
            if mIndex < kIndex then
                kIndex = kIndex - 1
            end
        end
        
        table.remove(l, kIndex)
        if kIndex < mIndex then
            mIndex = mIndex - 1
        end
        mIndex = mIndex - 1
        res = res..","
    end
    print(string.sub(res, 1, #res-1))
end