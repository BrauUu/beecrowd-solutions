n = int(input())

for _ in range(n):
    ax, ay, bx, by, cx, cy, dx, dy, rx, ry = list(map(int, input().split()))
    if ax > bx or ax != dx or ay != by or ay > dy or bx != cx or by > cy or dx > cx or dy != cy:
        print(0)
        continue
    if rx >= ax and rx <= bx and ry >= ay and ry <= cy:
        print(1)
        continue
    print(0)