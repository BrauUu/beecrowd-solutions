while True:
    x, y = list(map(int, input().split()))
    
    if x == y == 0:
        break
    
    print(x*3 - (x+y))