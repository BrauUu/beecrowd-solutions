while True:
    try:
        n = int(input())
        flag = False
        if n >= 0:
            root = int(n**(1/2))
            for i in range(root, -1, -1):
                n1 = (i) ** 2
                rest = n - n1
                n2 = rest ** (1/2)
                if n2.is_integer():
                    flag = True
                    break
        print('YES' if flag == True else 'NO')
    except:
        break    
    