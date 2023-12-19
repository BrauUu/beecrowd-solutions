t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    bgstCount = bgst = bgstSeq = 0
    for item in l:
        if item > bgst:
            bgstCount = 1
            bgst = item
            bgstSeq = 1
        elif item == bgst:
            bgstCount += 1
            if bgstCount > bgstSeq:
                bgstSeq = bgstCount
        else:
            bgstCount = 0
    print(f'Caso #{i+1}: {bgstSeq}')      