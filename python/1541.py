from math import sqrt, trunc


while True:
    x = input().split()
    
    if int(x[0]) == 0:
        break
    
    x1 = int(x[0])
    x2 = int(x[1])
    
    percentage = int(x[2])
    
    side = trunc(sqrt((x1 * x2) * 100 / percentage))
    
    print(side)
    
    