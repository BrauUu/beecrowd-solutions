l, n = list(map(int, input().split()))
d = {}

for _ in range(l):
    l1, l2 = input().split()
    d.update({l1: l2})
    
for _ in range(n):
    n1 = input()
    t = d.get(n1)
    if t:
        print(t)
    elif n1.endswith('y') and n1.endswith(('ay', 'ey', 'iy', 'oy', 'uy')) == False:
        print(n1[:-1] + 'ies')
    elif n1.endswith(('o', 's', 'ch', 'sh', 'x')):
        print(n1 + 'es')
    else:
        print(n1 + 's')