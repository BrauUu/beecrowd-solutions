while True:
    a, d = list(map(int, input().split()))
    
    if a == d == 0:
        break
    
    aList = list(map(int, input().split()))
    dList = list(map(int, input().split()))

    aList.sort()
    dList.sort()

    if aList[0] < dList[1]:
        print('Y')
        continue
    print('N')