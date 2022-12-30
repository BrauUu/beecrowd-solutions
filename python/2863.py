while True:
    try:
        n = int(input())
        lowestTime = 11.01
        for i in range(n):
            x = float(input())
            if x < lowestTime:
                lowestTime = x
                
        print(lowestTime)
    except:
        break