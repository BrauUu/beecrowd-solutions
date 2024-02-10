n, s = list(map(int, input().split()))
tl = []

for _ in range(n):
    t = input()
    tn, ts = t.rsplit(" ", maxsplit=1)
    if int(ts) > s:
        tl.append(tn)

print(*tl, sep="\n")