l, c = list(map(int, input().split()))
a, b = list(map(int, input().split()))
sallon = []
for _ in range(l):
    sallon.append(list(map(int, input().split())))

x, y = a - 1, b - 1
while True:
    sallon[x][y] = -1
    if y < c - 1 and sallon[x][y+1] == 1:
        x, y = x, y+1
    elif x < l - 1 and sallon[x+1][y] == 1:
        x, y = x+1, y
    elif y > 0 and sallon[x][y-1] == 1:
        x, y = x, y-1
    elif x > 0 and sallon[x-1][y] == 1:
        x, y = x-1, y
    else:
        print(f'{x + 1} {y + 1}')
        break