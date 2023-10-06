while True:
    try:
        n = int(input())
        l = list(map(int, input().split()))
        
        l.sort()
        v = 0
        
        g = len(l) - 1
        for i in range(int(g/2) + 1):
            v += l[g] - l[i]
            g -= 1
        print(v)
    except:
        break