while True:
    
    x = int(input())
    
    if x == 0:
        break
    
    count = 0
    g = x
    sum = 0
    
    while count < 5:
        if g % 2 == 0:
            sum += g
            count += 1
        g += 1
        
    print(sum)