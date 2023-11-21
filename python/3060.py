v = int(input())
n = int(input())

if v % n == 0:
    for _ in range(n):
        print(str(v//n))
else:
    rest = v % n
    for _ in range(rest):
        print(str(v//n + 1))
    for _ in range(n - rest):
        print(str(v//n))
    