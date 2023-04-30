n = int(input())

for g in range(n):
    
    arrLen = int(input())
    arr = list(map(int, input().split()))

    newArr = arr.copy()
    newArr.sort(reverse=True)

    cont = 0

    for i in range(arrLen):
        if arr[i] == newArr[i]:
            cont += 1
           
    print(cont)
    
