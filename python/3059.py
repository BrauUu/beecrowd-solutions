n, i, f = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort()
count = 0
for h in range(n):
    v = l[h]
    for g in range(n - 1, h, -1):
        v2 = l[g]
        s = v + v2
        if s <= f and s >= i:
            count += 1
            continue
        if s < i:
            break
print(count)