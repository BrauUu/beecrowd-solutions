j, r = list(map(int, input().split()))

data = list(map(int, input().split()))
res = [0 for i in range(j)]
for i in range(r*j):
    res[i%j] += data[i]

bigger = 0
biggerPos = 0
for i in range(j):
    item = res[i]
    if item >= bigger:
        bigger = item
        biggerPos = i

print(biggerPos + 1)