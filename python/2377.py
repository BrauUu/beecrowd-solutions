while True:
    try:
        l, d = list(map(int, input().split()))
        k, p = list(map(int, input().split()))
        
        print(int(l/d) * p + l*k)
        
    except:
        break
        