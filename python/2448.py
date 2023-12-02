n, m = list(map(int, input().split()))
houses = list(map(int, input().split()))
packages = list(map(int, input().split()))

def binarySearch(x, arr):
    return recursiveBinarySearch(x, arr, 0, len(arr) - 1)

def recursiveBinarySearch(x, arr, begin, end):
    middle = int((begin + end) / 2)
    
    if begin > end:
        return -1
    
    middleValue = arr[middle]
    
    if middleValue == x:
        return middle
    else:
        if middleValue < x:          
            begin = middle + 1
            pos = begin
        elif middleValue > x:
            end = middle - 1
            
        return recursiveBinarySearch(x, arr, begin, end)

time = 0
posInd = 0
for pkg in packages:
    ind = binarySearch(pkg, houses)
    time += abs(posInd - ind)
    posInd = ind
print(time)