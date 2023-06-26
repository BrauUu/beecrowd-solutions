matrix = [[1], [1,1,1]]
sumList = [1,3]

for i in range(2, 21):
    sum = 0
    matrix.append([])
    y = (i + 1) * 2 - 1
    for g in range(y):
        x = 0
        h = g - 1
        if g > 1:
            x += matrix[i-1][h-1]
        if g > 0 and g < y - 1:
            x += matrix[i-1][h]
        if g < y - 2:
            x += matrix[i-1][h+1]
        matrix[i].append(x)
        sum += x
    sumList.append(sum)
    
n = int(input())

print(sumList[n])
        

