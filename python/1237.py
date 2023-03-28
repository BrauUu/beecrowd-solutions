while True:
    try:
        x = str(input())
        y = str(input())
        
        if x == '' or y == '':
            break
        
        larger = 0
        
        for i in range(len(x)):
            temp = 0
            substr = x[i]
            j = i
            while y.count(substr) >= 1:
                temp += 1  
                j += 1
                if j >= len(x):
                    break
                substr += x[j]
            if temp > larger:
                larger = temp
                
        print(larger)
        
    except:
        break