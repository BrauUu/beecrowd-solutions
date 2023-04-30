def merge(arr, leftSide, rightSide):
    i = g = k = 0

    while len(leftSide) > i and len(rightSide) > g:
        leftSideItem = leftSide[i]
        rightSideItem = rightSide[g]

        if len(leftSideItem) >= len(rightSideItem):
            arr[k] = leftSideItem
            i += 1
        else:
            arr[k] = (rightSideItem)
            g += 1
        k += 1
        
    while i < len(leftSide):
        arr[k] = leftSide[i]
        i += 1
        k += 1

    while g < len(rightSide):
        arr[k] = rightSide[g]
        g += 1
        k += 1

def mergeSort(arr):
    arrLen = len(arr)
    if arrLen > 1:
        middle = arrLen // 2

        leftSide = arr[:middle]
        rightSide = arr[middle:]

        mergeSort(leftSide)
        mergeSort(rightSide)

        merge(arr, leftSide, rightSide)
    
n = int(input())
    
for i in range(n):
    x = input().split()
    mergeSort(x)   
    res = '' 
    for item in x:
        res += item + ' '
    print(res.strip())