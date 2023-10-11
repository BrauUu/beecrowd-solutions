n = int(input())

for i in range(n):
    x = int(input())
    x = bin(x)
    print(x.count('1'))