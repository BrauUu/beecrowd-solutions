while True:
    try:
        x = input()
        p = int(input())
        
        count = 0
        countR = 0
        
        for i in range(len(x)):
            if x[i] == 'W':
                count += 1
                countR = 0
            elif x[i] == 'R':
                if countR == 0:
                    count += 1
                elif countR == p:
                    count += 1
                    countR = 0
                countR += 1  
        print(count) 
    except:
        break