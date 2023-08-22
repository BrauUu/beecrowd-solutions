n = int(input())

l = list(map(int, input().split()))
l.sort()

x = 0

for i in range(n):
    if i > len(l) - 1:
        x = i + 1
        break
    if l[i] != i + 1:
        x = i + 1
        break
    
print(x)