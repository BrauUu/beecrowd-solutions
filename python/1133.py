x = int(input())
y = int(input())

if x > y:
    z = y
    w = x
else:
    z = x
    w = y

for i in range(z + 1, w):
    if i % 5 == 2 or i % 5 == 3:
        print(i)