while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(1, n + 1):
        v = n - i + 1
        x = v * v
        count += x
    
    print(count)