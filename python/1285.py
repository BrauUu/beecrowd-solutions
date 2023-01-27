while True:
    try:
        n, m = input().split()
        n = int(n)
        m = int(m)
        
        diff = m + 1 - n
        
        count = 0
        
        for i in range(n, m + 1):
            flag = False
            x = str(i)
            for g in range(len(x) - 1):
                if x.count(x[g]) > 1:
                   count += 1
                   break
                
        print(diff - count)
        
    except:
        break