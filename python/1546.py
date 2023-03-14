n = int(input())

for i in range(n):
    k = int(input())
    
    for g in range(k):
        x = int(input())
        
        name = ''
        
        if x == 1:
            name = 'Rolien'
        elif x == 2:
            name = 'Naej'
        elif x == 3:
            name = 'Elehcim'
        elif x == 4:
            name = 'Odranoel'
            
        print(name)