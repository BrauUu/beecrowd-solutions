while True:
    try: 
        exp = input()
        
        if exp == '':
            break
        
        if exp.count('(') == exp.count(')'):
            if exp.find('(') < exp.find(')') and exp.rfind('(') < exp.rfind(')'):
                print('correct')
                continue
        print('incorrect')
    
    except:
        break