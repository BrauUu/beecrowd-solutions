while True:
    p, n, c = list(map(int, input().split()))
    if p == n == c == 0:
        break
    l = ['' for i in range(p)]
    for i in range(n):
        x = input().split()
        for g in range(p):
            l[g] += x[g]
    
    resCount = 0
    
    for i in range(p):
        count = 0
        for g in range(n):
            if l[i][g] == '0':
                if count >= c:
                    resCount += 1
                count = 0
            elif l[i][g] == '1':
                count += 1
            
            if g == n - 1:
                if count >= c:
                    resCount += 1
    
    print(resCount)