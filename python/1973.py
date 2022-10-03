n = int(input())

arr = input().split()
sum = 0

for i in range(len(arr)):
    arr[i] = int(arr[i])
    sum += arr[i]
    
actualStar = 0
starCount = 1
sheepStolenCount = 0
    
while True:
    if actualStar < 0 or actualStar >= len(arr) or arr[actualStar] == 0:
        break
    
    if starCount < actualStar + 1:
        starCount = actualStar + 1

    if arr[actualStar] % 2 == 0:
        arr[actualStar] -= 1
        actualStar -= 1
    elif arr[actualStar] % 2 == 1:
        arr[actualStar] -= 1
        actualStar +=1
    sheepStolenCount += 1
    
print(starCount, sum - sheepStolenCount)
    

    
    