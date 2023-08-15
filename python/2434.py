n, v = list(map(int, input().split()))

smallestV = v

for i in range(n):
    x = int(input())
    v += x
    if v < smallestV:
        smallestV = v

print(smallestV)