n = int(input())

for i in range(n):
    t = input()
    r,g,b = input().split()
    r = int(r)
    g = int(g)
    b = int(b)
    
    value = ''
    
    if t == 'eye':
        value = r / 100 * 30 + g / 100 * 59 + b / 100 * 11
    elif t == 'mean':
        value = (r + g + b)/3
    elif t == 'max':
        value = [g, b, r]
        value = max(value)
    elif t == 'min':
        value = [g, b, r]
        value = min(value)
    print(f'Caso #{i+1}: {int(value)}')