def func(x):
    if x <= 1:
        return 0
    return func(x/2) + 1
        

t = int(input())    

for i in range(t):

    x = float(input())

    print(f'{func(x)} dias')