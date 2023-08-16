from math import sqrt

while True:

    n = int(input())
    if n == 0:
        break
    
    res = ''
    x = 1
    while x ** 2 <= n:
        res += str(x ** 2) + ' '
        x += 1
        
    print(res.strip())        