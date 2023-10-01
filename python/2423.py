a, b, c = list(map(int, input().split()))

ra = int(a / 2)
rb = int(b / 3)
rc = int(c / 5)

r = ra if ra <= rb and ra <= rc else rb if rb <= ra and rb <= rc else rc

print(r)