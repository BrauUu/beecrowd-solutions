while True:
    try:
        x = input()
        
        l = [0 for i in range(10)]
        biggest = 0
        biggestInd = 0
        
        for char in x:
            ind = int(char)
            l[ind] += 1
            temp = l[ind]
            if temp > biggest:
                biggest = temp
                biggestInd = ind
            elif temp == biggest and ind > biggestInd:
                biggestInd = ind
        
        print(biggestInd)
    except:
        break