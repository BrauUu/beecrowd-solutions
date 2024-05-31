n = int(input())

for _ in range(n):
    at, dt, bt, bd = list(map(int, input().split()))
    h = int(input())
    actualTime = 0
    while True:
        if actualTime % dt == 0:
            h = h - at
            if h <= 0:
                w = 'Andre'
                break
        if actualTime % bd == 0:
            h = h - bt
            if h <= 0:
                w = 'Beto'
                break
        actualTime += 1
    print(w)