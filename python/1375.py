while True:
    n = int(input())
    
    if n == 0:
        break
    
    l = [0 for _ in range(n)]
    flag = False
    
    for i in range(n):
        c, p = list(map(int, input().split()))
        pos = i + p
        if flag == False:
            if pos < 0 or pos > n - 1 or l[pos] != 0:  
                flag = True
            else:      
                l[pos] = c
    if flag:
        print('-1')
    else:
        res = ''
        for item in l:
            res += str(item) + ' '
        print(res.strip())