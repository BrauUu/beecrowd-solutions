while True:
    try:
        h, m = list(map(int, input().split()))
        qt = h * 60 // m
        xs = list(map(float, input().split()))
        avg = sum(xs) / qt
        res = 0
        for x in xs:
            res += (x - avg)**2
        res = (res/(qt-1))**(1/2)
        print(f'{res:.5f}')
    except:
        break