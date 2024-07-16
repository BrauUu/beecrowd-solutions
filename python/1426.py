n = int(input())

for _ in range(n):
    wall = []
    for i in range(1, 10):
        wall.append([])
        if i % 2 != 0:
            values = list(map(int, input().split()))
            for j in range(len(values)):
                value = values[j]
                wall[i-1].append(value)
                if j + 1 < len(values):
                    wall[i-1].append('X')
            continue
        for _ in range(i):
            wall[i-1].append('X')
    for i in range(0, len(wall) - 1, 2):
        row = wall[i]
        for j in range(0, int(len(row) / 2 + 0.99) , 2):
            total = row[j]
            x = wall[i+2][j]
            y = wall[i+2][j+2]
            v = int((total-(x+y))/2)
            wall[i+2][j+1] = v
            wall[i+1][j] = v + x
            wall[i+1][j+1] = v + y

            g = -(j+1)
            total = row[g]
            x = wall[i+2][g]
            y = wall[i+2][g-2]
            v = int((total-(x+y))/2)
            wall[i+2][g-1] = v
            wall[i+1][g] = v + x
            wall[i+1][g-1] = v + y
        print(*row, sep=' ')
        print(*wall[i+1], sep=' ')
    print(*wall[-1], sep=' ')