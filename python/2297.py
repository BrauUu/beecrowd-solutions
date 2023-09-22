g = 1
while True:
    r = int(input())
    
    if r == 0:
        break
    
    ac = 0
    bc = 0
    
    for i in range(r):
        a, b = list(map(int, input().split()))
        ac += a
        bc += b
    
    print(f'Teste {g}')
    print('Beto' if bc > ac else 'Aldo')
    print()
    
    g += 1