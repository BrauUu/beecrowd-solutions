n, c = list(map(int, input().split()))
count = 0
flag = False
for n in range(n):
    s, e = list(map(int, input().split()))
    count += (e - s)
    if count > c:
        flag = True

print('S' if flag else 'N')