while True:
    try:
        x = input()
        agg = 0
        for i in range(9):
            agg += int(x[i]) * (i+1)
        rest = agg % 11
        d1 = rest if rest < 10 else 0
        agg = 0
        for i in range(9):
            agg += int(x[i]) * (9-i)
        rest = agg % 11
        d2 = rest if rest < 10 else 0
        print(f'{x[:3]}.{x[3:6]}.{x[6:]}-{d1}{d2}')
    except:
        break