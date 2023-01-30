while True:
    n, m = map(int, input().split())
    
    if n == m == 0:
        break
    
    arr = list(map(int, input().split()))

    count = 0
    
    for i in range(1, n + 1):
        if arr.count(i) > 1:
            count += 1 

    print(count)