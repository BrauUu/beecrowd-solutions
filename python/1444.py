from math import ceil

def func(x):
    x = ceil(x / 3)
    if x == 1:
        return x
    return func(x) + x

while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(0)
    elif n <= 3:
        print(ceil(n / 3))
    else:
        print(func(n))