while True:
    try:
        d, v1, v2 = list(map(int, input().split()))
        t = 0
        if v1 > v2:
            t = d/(v1 - v2)
        print(f'{t:.2f}' if t > 0 else 'impossivel')
    except:
        break