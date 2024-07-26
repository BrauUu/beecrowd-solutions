from math import sqrt

a, b, c, d = list(map(int, input().split()))
flag = False
i = 1
while True:
    j = i * a
    g = c // j
    if c % j == 0:
        if j % b != 0 and d % j != 0:
            print(j)
            flag = True
            break
        if j > 1 and g % b != 0 and d % g != 0 and g % a == 0:
            print(g)
            flag = True
            break
    if i >= g:
        break
    i += 1
        
if flag == False:      
    if c % b != 0 and d % c != 0 and c % a == 0:
        print(c)
    else:
        print(-1)