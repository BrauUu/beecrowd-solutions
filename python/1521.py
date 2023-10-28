while True:
    n = int(input())
    
    if n == 0:
        break
    
    l = list(map(int, input().split()))
    
    k = int(input())
    i = k - 1
    
    while True:
        j = l[i] - 1
        if j == i:
            print(j + 1)
            break
        i = j