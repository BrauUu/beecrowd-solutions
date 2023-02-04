n = int(input())

for i in range(n):
    x = input().strip()
    temp = ''
    lx = len(x)
    for g in range(lx):
        if x[g].isalpha() == True:
            charCode = ord(x[g])
            temp += chr(charCode + 3)
        else:
            temp += x[g]
            
    x = temp   
    x = x[::-1]
    half = int(lx / 2)
        
    temp = x[:half]
    
    for g in range(half, lx):
        charCode = ord(x[g])
        temp += chr(charCode - 1)
        
    x = temp
    print(x)
    
    
    
    
    
    
    