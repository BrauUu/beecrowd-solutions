from math import sqrt

while True:
    try:
        n = int(input())
        h, c, l = list(map(int, input().split()))
        cat1 = h * n
        cat2 = c * n
        hip = sqrt(cat1**2 + cat2**2)
        print(f'{hip*l/10000:.4f}')
    except:
        break