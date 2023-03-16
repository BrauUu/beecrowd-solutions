while True:
    
    x, y = list(map(int, input().split()))
    
    if x == y == 0:
        break
    
    res = x + y
    res = str(res).replace('0', '')
    
    print(res)