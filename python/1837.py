a, b = input().split()

a = int(a)
b = int(b)

for i in range(-(abs(a)) - 1, +(abs(a)) + 1):
    rest = a - (b*i)
    if b == 0:
        print(a, rest)
        break
    if  rest < abs(b) and rest >= 0:
        print(i, rest)
        break