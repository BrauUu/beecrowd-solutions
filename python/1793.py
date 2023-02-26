while True:
    n = int(input())
    
    if n == 0:
        break
    
    arr = list(map(int, input().split()))
    
    sum = 10
    
    for i in range(1, len(arr)):
        if arr[i-1] + 10 <= arr[i]:
            sum += 10
        elif arr[i-1] + 10 > arr[i]:
            sum += arr[i] - arr[i-1]
            
    print(sum)
        