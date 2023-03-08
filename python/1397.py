while True:
    n = int(input())
    
    if n == 0:
        break
    
    countX = 0
    countY = 0
    
    for i in range(n):
        x, y = list(map(int, input().split()))
        
        if x > y:
            countX += 1
        elif y > x:
            countY += 1
            
    print(f'{countX} {countY}')