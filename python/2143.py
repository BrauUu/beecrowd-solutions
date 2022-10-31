while True:
    t = int(input())
    if t == 0:
        break
    for i in range(t):
        n = int(input())
        order = ((n - 1) * 2) + 1 if n % 2 == 1 else ((n - 2) * 2) + 2
        print(order)