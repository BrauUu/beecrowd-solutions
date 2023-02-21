def convertToBase(v, vb, nb):
    try:
        value = 0
        res = 0
        
        if vb == 'bin':
            value = int(v, base=2)
        elif vb == 'dec':
            value = int(v)  
        elif vb == 'hex':
            value = int(v, base=16)
       
        if nb == 'bin':
            res = bin(value)[2:]
        elif nb == 'dec':
            res = value
        elif nb == 'hex':
            res = hex(value)[2:]
            
        return res
    except:
        return None
               
    
n = int(input())

for i in range(n):
    value, base = input().split()
    
    
    print(f'Case {i+1}:')
    
    if base == 'bin':
        print(f'{convertToBase(value, base, "dec")} dec')
        print(f'{convertToBase(value, base, "hex")} hex')
    elif base == 'dec':
        print(f'{convertToBase(value, base, "hex")} hex')
        print(f'{convertToBase(value, base, "bin")} bin')
    elif base == 'hex':
        print(f'{convertToBase(value, base, "dec")} dec')
        print(f'{convertToBase(value, base, "bin")} bin')
        
    print()
    
        
    