q, e = list(map(int, input().split()))
l = list(map(int, input().split()))
for _ in range(q):
    ci = int(input())
    if l.count(ci) != 0:
        print(0)
        l.append(ci)
        continue
    print(1)
    l.append(ci)