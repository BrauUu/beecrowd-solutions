g = 1
while True:
    n = int(input())
    
    if n == 0:
        break
    
    l = list(map(int, input().split()))
    
    print(f'Teste {g}')
    
    for i in range(n):
        if i + 1 == l[i]:
            print(l[i])
            print()
            break
    g += 1