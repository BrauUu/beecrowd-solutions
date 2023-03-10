n = int(input())

for i in range(n):
    x = input()
    y = input()
    z = input()
    
    z1 = z.find('_')
    z2 = z.rfind('_')
    
    if x[z1] == y[z2] or x[z2] == y[z1]:
        print('Y')
    else:
        print('N')