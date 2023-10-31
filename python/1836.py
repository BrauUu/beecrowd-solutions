from math import sqrt

n = int(input())

att = ['HP', 'AT', 'DF', 'SP']

for g in range(n):
    p, l = input().split()
    l = int(l)
    res = ''
    values = []
    for i in range(4):
        v = 0
        b, iv, ev = list(map(int, input().split()))
        if i == 0:
            v = ((iv + b + sqrt(ev) / 8 + 50) * l) / 50 + 10
        else:
            v = ((iv + b + sqrt(ev) / 8) * l) / 50 + 5
        values.append(int(v))
    
    print(f'Caso #{g + 1}: {p} nivel {l}')
    for i in range(4):
        print(f'{att[i]}: {values[i]}')