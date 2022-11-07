x, y = input().split()
x = int(x)
y = int(y)

xRes = 0
yRes = 0
isBreak = False
arr = []

for i in range(x):
    arr.append(input().split())  
        
for i in range(x):
    for g in range(y):
        if int(arr[i][g]) == 42:
            xRes = i + 1
            yRes = g + 1
            if i != 0 and g != 0:
                if int(arr[i - 1][g - 1]) != 7 or int(arr[i][g - 1]) != 7 or int(arr[i - 1][g]) != 7:
                    xRes = 0
                    yRes = 0
                    continue
            else: 
                xRes = 0
                yRes = 0
                continue
            if i != x - 1 and g != 0:
                if int(arr[i + 1][g]) != 7 or int(arr[i][g - 1]) != 7 or int(arr[i + 1][g - 1]) != 7:
                    xRes = 0
                    yRes = 0
                    continue
            else: 
                xRes = 0
                yRes = 0
                continue
            if i != x -1 and g != y - 1:
                if int(arr[i + 1][g]) != 7 or int(arr[i + 1][g + 1]) != 7 or int(arr[i][g + 1]) != 7:
                    xRes = 0
                    yRes = 0
                    continue
            else: 
                xRes = 0
                yRes = 0
                continue
            if i != 0 and g != y - 1:
                if int(arr[i - 1][g]) != 7 or int(arr[i - 1][g + 1]) != 7 or int(arr[i][g + 1]) != 7:
                    xRes = 0
                    yRes = 0
                    continue
            else: 
                xRes = 0
                yRes = 0
                continue
            if xRes != 0 and yRes != 0:
                isBreak = True
                break
    if isBreak:
        break
            

print(xRes, yRes)
    