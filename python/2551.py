while True:
    try:
        n = int(input())
        
        record = 0
        
        for i in range(n):
            t, d = input().split()
            
            v = int(d) / int(t)
            
            if v > record:
                record = v
                print(i+1)
    except:
        break