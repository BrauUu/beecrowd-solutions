def fat(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum

while True:
    x = int(input())
    
    if x == 0:
        break
    
    xLen = len(str(x))
    j = 1
    sum = 0
    
    for i in range(xLen, 0, -1):
        sum += int(str(x)[i - 1]) * fat(j)
        j += 1
        
    print(sum)