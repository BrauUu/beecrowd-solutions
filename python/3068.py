tCount = 0
while True:
    try:
         
        x1, y1, x2, y2 = input().split()
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        
        if x1 == y1 == x2 == y2 == 0:
            break
        
        n = int(input())
        
        count = 0
        
        for i in range(n):
            x, y = input().split()
            x = int(x)
            y = int(y)
            
            if x >= x1 and x <= y1 and x <= x2 and x >= y2:
                count += 1
                
        tCount += 1
        
        print(f'Teste {tCount}')
        print(count)
        
    except:
        break