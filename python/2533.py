while True:
    try:
        x = int(input())
        
        sumNxC = 0
        sumC = 0

        for i in range(x):
            n, c = input().split()
            sumNxC += int(n) * int(c)
            sumC += int(c)
            
        print(f'{((sumNxC)/(sumC * 100)):.4f}')
    except:
        break