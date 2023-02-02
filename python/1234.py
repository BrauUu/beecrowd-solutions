while True:
    try:
        x = input()
        y = ''
        
        flag = True
        
        for i in range(len(x)):
            if x[i] != ' ':
                if flag == True:
                    y += x[i].upper()
                    flag = False
                elif flag == False:
                    y += x[i].lower()
                    flag = True
            else:
                y += ' '
        
        print(y)                    
        
    except:
        break