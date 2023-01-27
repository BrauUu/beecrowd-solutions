while True:
    try:
        n, d = input().split()
        n = int(n)
        d = int(d)
        
        if n == d == 0:
            break
        
        arr = [1 for x in range(n)]
        
        for i in range(d):
            x = input().split()
            for g in range(len(x)):
                if x[g] == '0':
                    arr[g] = 0
                    
        print('yes' if arr.count(1) > 0 else 'no')
    except:
        break 
    