while True:

    n = int(input())

    if n == 0:
        break

    trainA = input().split()
    obj = input().split()
    station = []
    trainB = []

    res = ''

    i = 0
    j = 0
    g = 0

    while i < len(trainA):
        station.append(trainA[i])
        res += 'I'
        if station[g] == obj[j]:
            trainB.append(station[g])
            station.pop(g)
            res += 'R'
            j += 1
            g -= 1
            h = g
            while h >= 0:
                if station[h] == obj[j]:
                    trainB.append(station[h])
                    station.pop(h)
                    res += 'R'
                    h -= 1
                    g -= 1
                    j += 1
                else:
                    break

        
        g += 1
        i += 1

    print(f'{res}{" Impossible" if obj != trainB else ""}')

