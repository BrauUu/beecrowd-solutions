while True:
    try:
        n, hMin, hMax = input().split()
        
        count = 0
        
        for i in range(int(n)):
            h = int(input())
            if h <= int(hMax) and h >= int(hMin):
                count += 1
                
        print(count)
        
    except:
        break