n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    
    count = 0
    g = x
    sum = 0
    
    while count < y:
        
        if g % 2 == 1:
            sum += g
            count += 1
            
        g += 1
        
    print(sum)