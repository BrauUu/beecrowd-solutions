v, t = list(map(int, input().split()))
l = list(map(int, input().split()))

for i in range(t):
    v += l[i]
    if v > 100:
        v = 100
    elif v < 0:
        v = 0

print(v)