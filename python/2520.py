while True:
    try:
        n, m = input().split()

        n = int(n)
        m = int(m)

        grid = []
        dest = {}
        org = {}

        for i in range(n):
            grid.append([])
            line = input().split()
            for g in range(m):
                item = int(line[g])
                grid[i].append(item)
                if item == 2:
                    dest = {'x': g, 'y': i}
                elif item == 1:
                    org = {'x': g, 'y': i}

        print(abs(dest['x'] - org['x']) + abs(dest['y'] - org['y']))
    except:
        break