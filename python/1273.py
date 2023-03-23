k = 0
while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    greatherstLen = 0
    for i in range(n):
        x = input()
        arr.append(x)
        lenX = len(x)
        if lenX > greatherstLen:
            greatherstLen = lenX
    if k >= 1:
        print()
    
    for item in arr:
        sep = ' '
        print(f'{sep * (greatherstLen - len(item)) + item}')
        
    k += 1
        