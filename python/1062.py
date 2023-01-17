while True:

    n = int(input())

    if n == 0:
        break

    while True:
        obj = input().split()
        trainA = [str(x) for x in range(1, len(obj) + 1)]
        if int(obj[0]) == 0:
            break
        station = []
        trainB = []

        i = 0
        j = 0
        g = 0

        while i < len(trainA):
            station.append(trainA[i])
            if station[g] == obj[j]:
                trainB.append(station[g])
                station.pop(g)
                j += 1
                g -= 1
                h = g
                while h >= 0:
                    if station[h] == obj[j]:
                        trainB.append(station[h])
                        station.pop(h)
                        h -= 1
                        g -= 1
                        j += 1
                    else:
                        break
            g += 1
            i += 1

        print("Yes" if trainB == obj else "No")
        
    print()

