while True:
    try:
        n = int(input())
        l = []
        for _ in range(n):
            l.append(tuple(input().split()))
        l.sort(key= lambda x: int(x[1]))
        res = []
        for item in l:
            res.append(item[0])
        print(*res, sep=' ')
    except:
        break