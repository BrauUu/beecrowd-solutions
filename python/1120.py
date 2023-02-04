while True:
    try:
        d, n = input().split()
        
        if d == n == '0':
            break
    
        x = ''
    
        for i in range(len(n)):
            if n[i] != d:
                x += n[i]
                
        try:
            x = int(x)
        except:
            x = 0
        
        print(x)
        
    except:
        break