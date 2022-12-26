from math import ceil

n = int(input())

for i in range(n):
    l = int(input())
    arr = input().split()
    intArr = [int(item) for item in arr if int(item) % 2 == 1]
    intArr.sort()

    res = ''
    
    x = len(intArr)
    y = ceil(x/2)

    for g in range(y):
        if g == y - 1 and g % 2 == 0 and len(intArr) % 2 == 1:
            res += f'{intArr[x - (g + 1)]}'
        else:
            if g == y - 1:
                res += f'{intArr[x - (g + 1)]} '
                res += f'{intArr[g]}'
            else:
                res += f'{intArr[x - (g + 1)]} '
                res += f'{intArr[g]} '
                
    print(res)
