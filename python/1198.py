while True:
    try:
        
        x, y = list(map(int, input().split()))
        
        print(abs(x-y))
        
    except:
        break