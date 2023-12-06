count = 1
while True:
    n = int(input())
    if n == 0:
        break
    l = []
    bgst = 0
    for _ in range(n):
        c, m = list(map(int, input().split()))
        if m > bgst:
            l.clear()
            l.append(c)
            bgst = m
        elif m == bgst:
            l.append(c)
            
    print(f'Turma {count}')
    print(*l, sep=" ", end=" ")
    print('\n')
    count += 1