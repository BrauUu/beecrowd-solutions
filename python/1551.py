n = int(input())

for i in range(n):
    x = input()
    x = x.replace(' ', '')
    x = x.replace(',', '')
    
    arr = []
    
    for g in range(len(x)):
        item = x[g]
        try:
            flag = arr.index(item)
        except:
            arr.append(item)
            
    force = len(arr)
    msg = ''
    
    if force < 13:
        msg = 'frase mal elaborada'
    elif force == 26:
        msg = 'frase completa'
    else:
        msg = 'frase quase completa'
        
    print(msg)