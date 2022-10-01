x = int(input())

for i in range(x):
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    
    sum = 0
    
    if n1 > n2:
        y = n1
        z = n2
    else:
        y = n2
        z = n1
    
    for g in range(z + 1, y, 1):
        if g % 2 == 1:
            sum += g
            
    print(sum)