n = int(input())

for i in range(n):
    obj = {}
    
    x = input().replace(' ', '').lower()
    
    for char in x:
        v = obj.get(char)
        if v == None:
            obj.update({char: 1})
        elif v != None:
            obj.update({char: int(v) + 1})
            
    largest = 0
    arr = []
            
    for item in obj:   
        v = obj.get(item)
        v = int(v) if v != None else 0
        if v > largest:
            arr.clear()
            arr.append(item)
            largest = v
        elif v == largest:
            arr.append(item)
        
    arr.sort()
    res = ''
    
    for x in arr:
        res += x
    
    print(res)
            