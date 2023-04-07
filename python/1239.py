while True:
    try:
        x = input()
        if x == '':
            break
        
        flagBold = False
        flagItalic = False
        res = ''
        
        for i in range(len(x)):
            char = x[i]
            if char == '_':
                if flagItalic == False:
                    res += '<i>'
                    flagItalic = True
                else:
                    res += '</i>'
                    flagItalic = False
            elif char == '*':
                if flagBold == False:
                    res += '<b>'
                    flagBold = True
                else:
                    res += '</b>'
                    flagBold = False
            else:
                res += char
                
        print(res)
        
    except:
        break