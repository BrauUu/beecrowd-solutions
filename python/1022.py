from re import split

n = int(input())

for i in range(n):
    entries = input()
    
    signal = ''
    
    tempList = entries.split(' / ')
    if len(tempList) < 4:
        signal = tempList[1].split()[1]
    elif len(tempList) == 4:
        signal = '/'
    
    n1, d1, n2, d2 = split(r" [+-/*] \s*", entries) 
    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)
    
    res = ''
    r1 = ''
    r2 = ''
      
    # works on versions >= 3.10
      
    # match signal:
    #     case '+':
    #         r1 = n1*d2 + n2*d1
    #         r2 = d1*d2
    #         res = str(r1) + '/' + str(r2)
    #     case '-':
    #         r1 = n1*d2 - n2*d1
    #         r2 = d1*d2
    #         res = str(r1) + '/' + str(r2)
    #     case '*':
    #         r1 = n1*n2
    #         r2 = d1*d2
    #         res = str(r1) + '/' + str(r2)
    #     case '/':
    #         r1 = n1*d2
    #         r2 = n2*d1
    #         res = str(r1) + '/' + str(r2)
    
    if signal == '+':
        r1 = n1*d2 + n2*d1
        r2 = d1*d2
        res = str(r1) + '/' + str(r2)
    elif signal == '-':
        r1 = n1*d2 - n2*d1
        r2 = d1*d2
        res = str(r1) + '/' + str(r2)
    elif signal == '*':
        r1 = n1*n2
        r2 = d1*d2
        res = str(r1) + '/' + str(r2)
    elif signal == '/':
        r1 = n1*d2
        r2 = n2*d1
        res = str(r1) + '/' + str(r2)
        
    simplifiedRes = res
    
    for i in range(r1 if r1 >= r2 else r2, 1, -1):
        if r1 % i == 0 and r2 % i == 0:
            simplifiedRes = str(int(r1 / i)) + '/' + str(int(r2 / i))
            break
            
    print(f'{res} = {simplifiedRes}')