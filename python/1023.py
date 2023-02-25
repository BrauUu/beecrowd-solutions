j = 0

while True:
    j += 1
    n = int(input())
    
    if n == 0:
        break
    
    obj = {}
    totalQty = 0
    totalNb = 0
    
    for i in range(n):
        nb, qty = map(int, input().split())
        
        totalQty += qty
        totalNb += nb
        
        key = int(qty/nb)
        
        obj[key] = nb if obj.get(key) == None else obj.get(key) + nb 
    
    arr = []
    
    for x in obj.keys():
        arr.append(x)
    
    arr.sort()
     
    res = ''
    for x in arr:
        res += f'{obj[x]}-{x} '
    
    print(f'Cidade# {j}:' if j == 1 else f'\nCidade# {j}:')
    print(res.strip())
    print(f'Consumo medio: {totalQty / totalNb - 0.0049:.2f} m3.')