while True:
    n = int(input())
    
    if n == 0:
        break
    
    m = 1
    m2 = n + 1
    y = 1
    spaces = len(str(2 ** (n + (n-2)) if n > 2 else n))
    
    for i in range(1, n + 1):
        x = y
        line = ''
        for j in range(m, m2):
            line += ' ' * (spaces - len(str(x))) + str(x) + ' ' 
            if x == 1:
                x = 2
                y = 2
            x = 2 ** j
        y =  2 ** i
        m += 1
        m2 += 1
        
        print(line.rstrip())
    print()