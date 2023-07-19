while True:
    try:
        d = input()
        
        if d == '':
            break
        
        s = input()
        print('Resistente' if d.find(s) != -1 else 'Nao resistente')
    except:
        break