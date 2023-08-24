from math import ceil
t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    x = ceil((n -2) / 3) * ceil((m - 2)/3)
    print(x)
    
        