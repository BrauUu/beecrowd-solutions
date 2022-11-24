while True:
    try:
        n, id = input().split()
        n = int(n)
        
        count = 0
        
        for i in range(n):
            videoId, isLol = input().split()
            if videoId == id and isLol == '0':
                count += 1
                
        print(count)
    except:
        break