n = int(input())

for i in range(n):
    x = input()
    xLen = len(x)
    
    leftSide = x[:int((xLen - 1) / 2) + 1]
    rightSide = x[int((xLen) / 2):]
    
    res = ''
    res2 = ''
    
    for g in range(1, len(leftSide) + 1):
        res += leftSide[-g]
        res2 += rightSide[-g]
        
    print(f'{res + res2}')