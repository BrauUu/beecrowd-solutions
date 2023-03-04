n = int(input())

for i in range(n):
    a, b = input().split()
    flag = False
    
    if len(b) > len(a):
        flag = True
    
    if flag == False:
        for i in range(1, len(b) + 1):
            if b[-i] != a[-i]:
                flag = True
                break
        
    if flag == False:
        print('encaixa')
    else:
        print('nao encaixa')