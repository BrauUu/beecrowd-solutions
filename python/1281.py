n = int(input())

for i in range(n):
    
    obj = {}
    
    m = int(input())
    
    for g in range(m):
        key, value = input().split()
        
        obj.update({key : float(value)})
        
    m = int(input())
    
    sum = 0
    
    for g in range(m):
        fruit, qty = input().split()
        
        value = obj.get(fruit) or 0
        
        sum += int(qty) * value
        
    print(f'R$ {sum:.2f}')