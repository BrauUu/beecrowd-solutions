d, i, x, f = list(map(int, input().split()))

if d % 2 == 0:
    print(i if f % 2 == 0 else i - x)
else:
    print(i if f % 2 == 0 else i + x)