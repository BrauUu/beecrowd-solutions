from math import sqrt

c = int(input())

l = []
for i in range(2, 1001):
    count = 2
    for j in range(2, int(sqrt(i) + 1)):
        if i % j == 0:
            count += 1 if i/j == j else 2
    if count % 2 == 0:
        l.append(i)
        
for _ in range(c):
    n = int(input())
    while True:
        try:
            print(l.index(n) + 1)
            break
        except:
            n -= 1