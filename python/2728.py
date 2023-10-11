while True:
    try:
        x = input().lower().split('-')
        flag = True
        cobol = 'cobol'
        
        for i in range(len(x)):
            word = x[i]
            if word[0] != cobol[i] and word[-1] != cobol[i]:
                flag = False
                break
            
    
        print('GRACE HOPPER' if flag else 'BUG')
            
        
    except:
        break