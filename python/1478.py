while True:
    n = int(input())
    
    if n == 0:
        break
    
    for i in range(1, n + 1):
        line = ''
        x = i
        flag = False
        for j in range(n):
            line += ' ' * (3 - len(str(x))) + str(x) + ' '
            if x == 1:
                flag = True
            if flag == False:
                x -= 1
            else:
                x += 1
                
        print(line.rstrip())
    print()