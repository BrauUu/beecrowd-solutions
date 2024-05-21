while True:
    try:
        n = int(input())
        l = list(map(int, input().split()))
        l.sort()
        print(len(l) // 2, l[(len(l)) // 2] - l[(len(l) - 1) // 2])
    except:
        break