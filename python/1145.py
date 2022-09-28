x, y = input().split()

x = int(x)
y = int(y)

j = 0
while True:
    z = ''
    for i in range(x):
        j += 1
        if i == x - 1:
            z = z + str(j)
        else:
            z = z + str(j) + ' '
        if j >= y:
            break;
    print(z)
    if j >= y:
        break;