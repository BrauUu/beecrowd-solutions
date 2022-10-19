n = int(input())

for i in range(n):
    x = input().split()
    f1 = int(x[0])
    f2 = int(x[1])
    
    mdc = 0
    
    y = 0
    z = 0
    
    if f1 < f2:
        y = f1
        z = f2
    else:
        y = f2
        z = f1
            
    while True:
        w = z % y
        if w == 0:
            break
        z = y
        y = w
        
    print(y)