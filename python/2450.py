def isLineAllZero(list, ind):
        return l[i].count(0) == m

n, m = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
    
flag = flagZeroLine = False
initG = initH = 0

for i in range(n):
    flagActualZeroLine = False
    if flag:
        break
    if isLineAllZero(l, i):
        flagActualZeroLine = True
        flagZeroLine = True
        continue
    if flagZeroLine != flagActualZeroLine:
        flag = True
        break
    
    flagLineChecked = False
    for g in range(initG, m, 1):
        for h in range(initH, n):
            if h == i:
                if l[h][g] != 0:
                    flagLineChecked = True
                    initG = g + 1
                    initH = h + 1
            if g > 0:
                if l[h][g-1] != 0:
                    flag = True
                    break
            if h > i:
                if l[h][g] != 0:
                    flag = True
        if flagLineChecked:
            break 

print('N' if flag else 'S')
      
            
        