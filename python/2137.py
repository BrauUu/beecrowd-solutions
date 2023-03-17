while True:
    try:
        n = int(input())
        
        arr = []
        
        for i in range(n):
            arr.append(input())
            
        arr.sort()
        
        for item in arr:
            print(item)
            
    except:
        break