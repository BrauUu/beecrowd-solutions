while True:
    n = int(input())
    
    temp = n
    res = ''
    while temp > 0:
        rest = temp % 32
        div = temp // 32
        temp = div
        
        if rest > 9:
            rest = chr(65 + rest - 10)
        
        res = str(rest)  + res    
        
    print(res or 0)  
    
    if n == 0:
        break