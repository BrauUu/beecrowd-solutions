while True:    
    l, c, p = list(map(int, input().split()))
    lab = []
    if l == c == p == 0:
        break
    for _ in range(l):
        lab.append(list(map(int, input().split())))

    pos = p - 1
    boom = False

    for i in range(l):
        rFlag = lFlag = False
        r = l = rPos = lPos = 0
        for j in range(1, c):
            if rFlag == lFlag == True:
                break
            if rFlag == False and pos + j < c and lab[i][pos + j] != 0:
                r = lab[i][pos + j]
                rPos = pos + j
                rFlag = True
            if lFlag == False and pos - j > -1 and lab[i][pos - j] != 0:
                l = lab[i][pos - j]
                lPos = pos - j
                lFlag = True
        pos = pos + (l-r)
        if pos <= lPos:
            print(f'BOOM {i+1} {lPos + 1}')
            boom = True
            break
        elif pos >= rPos:
            print(f'BOOM {i+1} {rPos + 1}')
            boom = True
            break
    
    if boom == False:
        print(f'OUT {pos + 1}')