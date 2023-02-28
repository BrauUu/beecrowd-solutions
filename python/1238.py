n = int(input())

for i in range(n):
    x, y = input().split()
    
    res = ''
    
    z = len(x) if len(x) > len(y) else len(y)
    
    for i in range(z):
        res += x[i] if i < len(x) else ''
        res += y[i] if i < len(y) else ''
        
    print(res)