from math import ceil
res = ''

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
    
g = 0
while True:
    g += 1
    n, q = map(int, input().split())
    
    if n == q == 0:
        break
    
    arr = []
    
    for i in range(n):
        arr.append(int(input()))
        
    arr.sort()
    
    print(f'CASE# {g}:')
    
    for i in range(q):
        x = int(input())
        
        pos = binarySearch(x, arr)
        newPos = pos
        
        if pos != -1:
            while newPos > 0 and arr[newPos - 1] == arr[pos]:
                newPos -= 1

        print(f'{x} found at {newPos + 1}' if pos != -1 else f'{x} not found')
        

