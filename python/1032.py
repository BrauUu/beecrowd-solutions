def removeZeros(arr):
    while True:
        try:
            arr.remove(0)
        except:
            break

while True:
    n = int(input())
    if n == 0:
        break
    arr = [x for x in range(1, n + 1)]
    primos = [2, 3, 5, 7, 11]
    primos.extend(x for x in range(100) if x % 2 != 0 and x %
                  3 != 0 and x % 5 != 0 and x % 7 != 0 and x % 11 != 0)

    actualPos = -1
    m = 0
    x = actualPos

    while len(arr) > 1:
        x = primos[m]
        actualPos += x
        while actualPos > len(arr) - 1:
            actualPos -= len(arr)
            removeZeros(arr)
        arr[actualPos] = 0 
        if len(arr) == 2:
            removeZeros(arr)
        m += 1    
        
    print(arr)