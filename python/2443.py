a, b, c, d = list(map(int, input().split()))

x = (a * d) + (c * b)
y = (b * d)

for i in range(y, 1, -1):
    if x % i == 0 and y % i == 0:
        x = int(x / i)
        y = int(y / i)
        break

print(x, y)