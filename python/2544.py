from math import sqrt

while True:
    try:
        n = int(input())
        count = 0
        while n >= 2:
            n = n / 2
            count += 1
        print(count)
    except:
        break