n, l = list(map(int, input().split()))

arr = [-1 for _ in range(n)] 
i = 0
for _ in range(l):
    x, y = list(map(int, input().split()))
    smlst = arr[x-1] if arr[x-1] < arr[y-1] else arr[y-1]
    bgst = arr[x-1] if arr[x-1] > arr[y-1] else arr[y-1]
    if smlst == bgst == -1:
        arr[x-1] = i
        arr[y-1] = i
        i += 1
    elif smlst != bgst:
        if smlst == -1:
            arr[x-1] = bgst
            arr[y-1] = bgst
        else:
            while True:
                try:
                    ind = arr.index(bgst)
                    arr[ind] = smlst
                except:
                    break

print('COMPLETO' if arr.count(0) == n else "INCOMPLETO")