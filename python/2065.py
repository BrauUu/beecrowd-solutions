def getFreeEmployeeIndex(n):
    ind = 0
    lowest = vt[0] 
    for i in range(n):
        if vt[i] < lowest:
            lowest = vt[i]
            ind = i
    return ind

n, m = list(map(int, input().split()))

vt = [0 for i in range(n)]

v = list(map(int, input().split()))
c = list(map(int, input().split()))

count = 0

for i in range(m):
    freeEmployeeIndex = count
    if count >= n:
        freeEmployeeIndex = getFreeEmployeeIndex(n)
    vt[freeEmployeeIndex] += v[freeEmployeeIndex] * c[i]
    count += 1

print(sorted(vt, reverse=True)[0])