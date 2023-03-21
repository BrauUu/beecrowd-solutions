while True:
    n = int(input())
    
    if n == 0:
        break
    
    arr = list(map(int, input().split()))
    
    biggest = 0
    secondBiggest = 0
    
    for i in range(len(arr)):
        item = arr[i]
        if item > biggest:
            temp = biggest
            biggest = item
            secondBiggest = temp
        elif item > secondBiggest:
            secondBiggest = item
            
    print(arr.index(secondBiggest) + 1)
