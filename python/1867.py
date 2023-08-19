while True:
    n, m = input().split()
    
    if n == m == '0':
        break
    
    while len(n) != 1 or len(m) != 1:
        sumN = 0
        sumM = 0
        lenN = len(n)
        lenM = len(m)
        for i in range(lenN if lenN > lenM else lenM):
            sumN += int(n[i] if i < lenN else 0)
            sumM += int(m[i] if i < lenM else 0) 
        n = str(sumN)
        m = str(sumM)
    if int(n) > int(m):
        print(1)
    elif int(m) > int(n):
        print(2)
    else:
        print(0)
        
        