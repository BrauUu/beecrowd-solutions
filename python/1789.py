while True:
    try:
        l = int(input())
        arr = input().split()
        
        for i in range(l):
            arr[i] = int(arr[i])
            
        arr.sort()  
                  
        if arr[len(arr) - 1] < 10:
            print(1)
        elif arr[len(arr) - 1] >= 10 and arr[len(arr) - 1] < 20:
            print(2)
        elif arr[len(arr) - 1] >= 20:
            print(3)
    except:
        break