def func(x):
    if x == 1:
        return 1
    elif x % 2 == 0:
        return func(x - 1) + (x)
    elif x % 2 == 1:
        return func(x - 1) + (x + 1)

t = int(input())    

for i in range(t):

    x = int(input())

    print(func(x))