nc = int(input())

for i in range(nc):
    values = input().split()
    
    n = int(values[0])
    k = int(values[1])
    
    arr = []
    
    for j in range(1, n + 1):
        arr.append(j)
    
    g = -1
    while True:
        g += k
        if g > len(arr) - 1:
            g = g - (g - (g % len(arr) ))
        if len(arr) == 1:
            print(f'Case {i + 1}: {arr[0]}')
            break
        arr.pop(g)
        g -= 1
        
        