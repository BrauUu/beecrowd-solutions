while True:
    x, y = input().split()
    y = int(y)
    x = int(x)
    
    if x == 0 and y == 0:
        break
    
    print(x * y)