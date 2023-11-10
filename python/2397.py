l = list(map(int, input().split()))
l.sort()
a, b, c = l

cond1 = abs(b - c) < a and a < b + c
cond2 = abs(a - c) < b and b < a + c
cond3 = abs(b - a) < c and c < a + b

if cond1 and cond2 and cond3:
    p = a ** 2 + b ** 2
    if p == c ** 2:
        print('r')
    elif p > c ** 2:
        print('a')
    else:
        print('o')
else:
    print('n')