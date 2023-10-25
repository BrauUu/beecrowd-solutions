while True:
    r = int(input())
    
    if r == 0:
        break
    
    m = list(map(int, input().split()))
    l = list(map(int, input().split()))
    mCount = lCount = mPoints = lPoints = lTemp = mTemp = 0
    flag = False
    for i in range(r):
        mItem = m[i]
        lItem = l[i]
        mPoints += mItem
        lPoints += lItem
        if mTemp == mItem:
            mCount += 1
        else:
            mCount = 1
            mTemp = mItem
        
        if lTemp == lItem:
            lCount += 1
        else:
            lCount = 1
            lTemp = lItem
            
        if flag == False:
            if mCount == lCount == 3:
                flag = True
            else:
                if lCount == 3:
                    lPoints += 30
                    flag = True
                elif mCount == 3:
                    mPoints += 30
                    flag = True
                    
    res = 'T'
                    
    if mPoints > lPoints:
        res = 'M'
    elif mPoints < lPoints:
        res = 'L'
                    
    print(res)