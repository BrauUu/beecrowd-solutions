def removeZeros(arr):
    while True:
        try:
            arr.remove(0)
        except:
            break
    return len(arr)

while True:
    n = int(input())
    m = 0
    if n == 0:
        break
    while True:
        m += 1
        arr = [x for x in range(1,n + 1)]
        actualPos = 0
        x = n

        while arr[actualPos] != 13:
            arr[actualPos] = 0
            actualPos += m
            while actualPos > x - 1:
                actualPos -= x
                x = removeZeros(arr)
            while arr[actualPos] == 0:
                actualPos += 1
                if actualPos > x - 1:
                    actualPos -= x
                    x = removeZeros(arr)
                    
        removeZeros(arr)         
        if len(arr) == 1:
            print(m)
            break
                
