while True:
    n = int(input())
    if n == 0:
        break
    kids = []
    for i in range(n):
        name, value = input().split()
        kids.append({'name' : name, 'value' : int(value)})
    
    actualPos = 0
    value = kids[actualPos]['value']
    while len(kids) > 1:
        x = value % len(kids)
        if value % 2 != 0:
            actualPos += x
        else:
            actualPos -= x 
        
        if actualPos >= len(kids):
            actualPos -= len(kids)
        elif actualPos < 0:
            actualPos = len(kids) + actualPos 
            
        value = kids[actualPos]['value']
        lf = kids.pop(actualPos)
        actualPos += -1 if value % 2 != 0 else 0
        
    w = kids[0]['name']
    print(f'Vencedor(a): {w}')