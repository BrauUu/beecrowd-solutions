p1, c1, p2, c2 = list(map(int, input().split()))

x = (p1 * c1) - (p2 * c2)

if x > 0:
    print(-1)
elif x < 0:
    print(1)
else:
    print(0)