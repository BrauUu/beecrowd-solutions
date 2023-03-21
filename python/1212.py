while True:
    x, y = input().split()
    if x == y == '0':
        break
    
    lenX = len(x)
    lenY = len(y)
    
    if lenX > lenY:
        y = y.rjust(lenX, '0')
    elif lenX < lenY:
        x = x.rjust(lenY, '0')   
    
    carry = False
    carryCount = 0
    
    for i in range(len(x) - 1, -1, -1):  
        
        itemX = x[i]
        itemY = y[i]
        
        sum = int(itemX) + int(itemY) + ( 1 if carry == True else 0)
        
        if sum >= 10:
            carryCount += 1
            carry = True
        else:
            carry = False
    
    msg = ''
    
    if carryCount > 1:
        msg = str(carryCount) + ' carry operations.'   
    elif carryCount == 1:
        msg = str(carryCount) + ' carry operation.'
    else:
        msg = 'No carry operation.'
        
    print(msg)