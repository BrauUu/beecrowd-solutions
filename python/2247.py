g = 1
while True:
    n = int(input())
    if n == 0:
        break

    l = []
    temp = 0
    
    for i in range(n):
        j, z = list(map(int, input().split()))
        l.append(temp + (j-z))
        temp = temp + (j-z)
        
    print(f'Teste {g}')
    for item in l:
        print(item)
    print()
    g += 1