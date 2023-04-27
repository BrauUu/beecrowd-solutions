from math import sqrt

n = int(input())

for i in range(n):
    x = int(input())
    sqrtX = int(sqrt(x))
    
    flag = False
    
    for j in range(2, sqrtX + 1):
        if x % j == 0:
            flag = True
            break 
        
    if flag == True:
        print('Not Prime')   
    else:
        print('Prime')