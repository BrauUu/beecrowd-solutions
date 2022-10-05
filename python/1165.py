n = int(input())

for i in range(n):
    
    x = int(input())
    
    count = 0
    
    for g in range(2, x):
        if x % g == 0:
            count += 1
            break
    
    if count > 0:
        print(f'{x} nao eh primo')
    else:
        print(f'{x} eh primo')