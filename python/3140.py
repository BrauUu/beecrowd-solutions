while True:
    try:
        
        x = input()
        
        if x == '':
            raise
        
        if x.find('<body>') != -1:
            while True:
                x = input()
                if x.find('</body>') == -1:
                    print(x)
                else:
                    break
        
    except:
        break