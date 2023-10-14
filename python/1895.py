n, t, l = list(map(int, input().split()))
m = t

a = b = 0

for i in range(n-1):
    s = int(input())
    dif = abs(m - s)
    if dif <= l:
        m = s
        p = dif
        if i % 2 == 0:
            a += p
        else:
            b += p
            
print(a, b)