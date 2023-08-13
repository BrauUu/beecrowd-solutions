from math import sqrt 

n = int(input())

for i in range(n):
    x = int(input())
    y = 1-4*-(x*2)
    print(int((-1 + sqrt(y))/2))