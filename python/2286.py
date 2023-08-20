count = 1
while True:
    try:
        n = int(input())
        
        if n == 0:
            break
        
        p1 = input()
        p2 = input()
        
        print(f'Teste {count}')
        
        for i in range(n):
            p1n, p2n = list(map(int, input().split()))
            s = p1n + p2n
        
            if s % 2 == 0:
                print(p1)
            else:
                print(p2)
        count += 1
        print()
    except:
        break