def fn(l, k, m):
    p = [[0 for _ in range(k+1)] for _ in range(m+1)]
    for i in range(1, m + 1):
        x, y = l[i-1]
        for j in range(k+1):
            if y > j:
                p[i][j] = p[i-1][j]
                continue
            p[i][j] = max(p[i-1][j], p[i-1][j-y] + x)  
    return p[-1][-1] 

n = int(input())

for _ in range(n):
    m = int(input())
    l = []
    for j in range(m):
        x, y = map(int, input().split())
        l.append((x, y))
    k = int(input())
    r = int(input())
    res = fn(l, k, m)
    if res >= r:
        print('Missao completada com sucesso')
    else:
        print('Falha na missao')