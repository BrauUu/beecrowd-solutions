n,  x = list(map(int, input().split()))

l = list(map(int, input().split()))

max = 1
viewsCount = 1

for i in range(len(l) - 1):
    y = l[i]
    z = l[i+1]
    diff = z - y
    if diff <= x:
        viewsCount += 1
    else:
        if viewsCount > max:
            max = viewsCount
        elif max == n:
            break
        viewsCount = 1

if viewsCount > max:
    max = viewsCount

print(max)