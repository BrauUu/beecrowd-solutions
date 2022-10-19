n = int(input())

for i in range(n):
    x = int(input())
    
    if x < 2014:
        print(f'{2014 - x + 1} D.C.')
    else:
        value = x - 2014
        if value == 0:
            print(f'{value + 1} D.C.')
        else:
            print(f'{value} A.C.')