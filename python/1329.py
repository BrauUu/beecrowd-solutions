while True:
    try:
        n = int(input())
        
        if n == 0:
            break
        
        x = input().split()
        
        countM = 0
        countJ = 0
        
        for item in x:
            if item == '0':
                countM += 1
            elif item == '1':
                countJ += 1
        
        print(f'Mary won {countM} times and John won {countJ} times')
    
    except:
        break