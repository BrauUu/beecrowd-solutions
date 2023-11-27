while True:
    n = int(input())
    if n == 0:
        break
    v = [i for i in range(1, n+1)]
    l = []
    j = 0
    while l != v:
        j += 1
        l = list(map(int, input().split()))
    print(j)