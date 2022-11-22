while True:
    try:
        n, q = input().split()
        n = int(n)
        q = int(q)
        
        arr = []
        
        for i in range(n):
            arr.append(int(input()))
            
        arr.sort(reverse=True)
            
        for i in range(q):
            print(arr[int(input()) - 1])
        
    except:
        break