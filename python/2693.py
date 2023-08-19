while True:
    try:
        q = int(input())

        l = []

        for i in range(q):
            name, reg, dist = input().split()
            l.append((int(dist), reg, name))

        l = sorted(l, key=lambda x: (x[0], x[1], x[2]))

        for item in l:
            print(item[2])
    except:
        break