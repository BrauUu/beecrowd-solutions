n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    sum = 0
    m = arr[0]
    
    for j in range(1, m + 1):
        sum += arr[j]
        
    avg = sum / m
    
    count = 0
    
    for j in range(1, m + 1):
        if arr[j] > avg:
            count += 1
            
    print(f'{(count * 100 / m):.3f}%')