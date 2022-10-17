from math import floor

while True:
    x = int(input())

    if x == 0:
        break

    for i in range(1, x + 1):
        line = ''
        count = i if i <= floor(x / 2) else x + 1 - i
        value = 0
        for j in range(1, x + 1):
            if value > x + 1 - j:
                value -= 1
                if j == x:
                    line = line + str(value)
                else:
                    line = line + str(value) + '   '
            elif count > value:
                value += 1
                if j == x:
                    line = line + str(value)
                else:
                    line = line + str(value) + '   '
            elif j > count:
                if j == x:
                    line = line + str(value)
                else:
                    line = line + str(count) + '   '
                
        print(line)
    print()
