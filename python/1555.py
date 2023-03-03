n = int(input())

for i in range(n):
    x, y = list(map(int, input().split()))
    
    rRes = pow(3*x, 2) + pow(y, 2)
    bRes = 2 * pow(x, 2) + pow(5 * y, 2)
    cRes = -100 * x + pow(y, 3)
    
    if rRes > bRes and rRes > cRes:
        print('Rafael ganhou')
    elif bRes > rRes and bRes > cRes:
        print('Beto ganhou')
    elif cRes > rRes and cRes > bRes:
        print('Carlos ganhou')