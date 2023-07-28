def orderByModule(x,m):
    return (x % m if x > 0 else -(abs(x) % m), x % 2 == 0, -x if x % 2 == 1 else x)

flag = False
while True:
    n, m = list(map(int, input().split()))
    
    if n == m == 0:
        flag = True
    
    if flag != True:
        numbersList = []
        
        for i in range(n):
            numbersList.append(int(input()))
        
        numbersListOrdered = sorted(numbersList, key=lambda x : orderByModule(x, m))
    
        print(n, m)
    
        for number in numbersListOrdered:
            print(number)
    else:
        print(n, m)
        break