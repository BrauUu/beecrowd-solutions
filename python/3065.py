count = 0
while True:
    n = int(input())
    count += 1
    if n == 0:
        break
    
    x = input()     
    j = 0
    res = 0
    actualSignal = ''
    
    if len(x) == 1:
        res = int(x)
    
    for g in range(1, len(x)):
            
        if x[g] == '+': 
            if actualSignal == '+':
                res += int(x[j:g])
            elif actualSignal == '-':
                res -= int(x[j:g])
            else:
                res = int(x[j:g])   
            actualSignal = '+'
            j = g + 1
        elif x[g] == '-': 
            if actualSignal == '+':
                res += int(x[j:g])
            elif actualSignal == '-':
                res -= int(x[j:g])
            else:
                res = int(x[j:g])   
            actualSignal = '-'
            j = g + 1
        elif g == len(x) - 1: 
            if actualSignal == '+':
                res += int(x[j:])
            elif actualSignal == '-':
                res -= int(x[j:])
            else:
                res = int(x[j:])
    print(f'Teste {count}\n{res}\n')
        
            