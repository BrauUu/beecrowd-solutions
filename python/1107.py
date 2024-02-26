while True:
    a, c = list(map(int, input().split()))
    if a == c == 0:
        break
    l = list(map(int, input().split()))
    pItem = a
    count = 0
    for item in l:
        if item < pItem:
            count += (pItem - item)
        pItem = item
    
    print(count)