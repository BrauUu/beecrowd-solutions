c = int(input())

for i in range(c):
    x = input().split()
    
    name = x[0]
    force = x[1]
    
    if name == 'Thor':
        print('Y')
    else:
        print('N')