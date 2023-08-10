while True:
    n = int(input())
    
    if n == 0:
        break
    
    rectangleCount = 0
    pairsCount = 0
    
    for i in range(n):
        c, v = list(map(int, input().split()))
        pairsCount += int(v / 2)
        if pairsCount >= 2:
            temp = int(pairsCount / 2)
            rectangleCount += temp
            pairsCount = pairsCount - (temp * 2)
    
    print(rectangleCount)
            
            
        