while True:
    n = int(input())
    if n == 0:
        break
    fink = picapau = 0
    c = n
    i = 1
    while c > 0:
        picapau += 1
        c -= 1
        fink += i
        c -= i
        i += 1
    picapau = n - fink
    print(fink, picapau)