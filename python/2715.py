while True:
    try:
        n = int(input())
        
        values = input().split()
        
        lowestDiff = 0
        x = int((len(values) - 1) / 2)
        max = (len(values) - 1)
        min = 0
        
        if len(values) == 1:
            print(values[0])
        
        while True:
            sumBottom = 0
            sumUpper = 0
            for j in range(len(values)):
                if j <= x:
                    sumBottom += int(values[j])
                else:
                    sumUpper += int(values[j])
                    
            diff = abs(sumBottom - sumUpper)
            
            if sumBottom == sumUpper:
                lowestDiff = 0
                break
            elif min == max or min > max:
                if diff < lowestDiff:
                    lowestDiff = diff
                break
            elif sumBottom > sumUpper:
             max = x - 1 if x >= 1 else 0
            elif sumBottom < sumUpper:
                min = x + 1 if x < len(values) - 1 else 0
                
            if diff < lowestDiff or x == int((len(values) - 1) / 2) :
                lowestDiff = diff 
            
            x = int((max + min) / 2)
           
        print(lowestDiff)
            
    except:
        break