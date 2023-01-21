while True:
    n = int(input())
    
    if n == 0:
        break
    
    arr = input().split()
    newArr = [int(item) for item in arr]
    count = 0
    
    for i in range(n):
        if i == 0:
            if newArr[i] > newArr[n - 1] and newArr[i] > newArr[i+1] or newArr[i] < newArr[n - 1] and newArr[i] < newArr[i+1]:
                count += 1
        elif i == n -1:
            if newArr[i] > newArr[i - 1] and newArr[i] > newArr[0] or newArr[i] < newArr[i - 1] and newArr[i] < newArr[0]:
                count += 1
        elif newArr[i] > newArr[i - 1] and newArr[i] > newArr[i+1] or newArr[i] < newArr[i - 1] and newArr[i] < newArr[i+1]:
            count += 1
            
    print(count)