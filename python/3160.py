l = list(input().split())
nl = list(input().split())
f = input()

nfl = []

for _ in range(len(l)):
    friend = l[0]
    if friend == f:
        break
    temp = l.pop(0)
    nfl.append(temp)

nfl.extend(nl)
nfl.extend(l)

print(*nfl)