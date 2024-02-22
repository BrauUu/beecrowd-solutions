while True:
    try:
        m, n = list(map(int, input().split()))
        s = 0
        for _ in range(m):
            s += sum(list(map(int, input().split())))
        
        bagsCount = s // 60
        litersCount = s % 60

        print(f'{bagsCount} saca(s) e {litersCount} litro(s)')
    except:
        break