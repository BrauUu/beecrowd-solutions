n, m = list(map(int, input().split()))

pos = list(0 for _ in range(n))
for _ in range(m):
    p, d = list(map(int, input().split()))
    p -= 1
    i = 1
    pos[p] = 1
    while True:
        r = p + d * i
        l = p - d * i
        if r < n:
            pos[r] = 1
        if l >= 0:
            pos[l] = 1
        elif r >= n and l < 0:
            break
        i += 1

for i in pos:
    print(i)