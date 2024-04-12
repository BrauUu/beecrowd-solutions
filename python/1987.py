while True:
    try:
        n, m = input().split()
        s = 0
        for num in m:
            s += int(num)
        print(f'{s} {"sim" if s % 3 == 0 else "nao"}')
    except:
        break