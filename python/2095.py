s = int(input())

qList = sorted(list(map(int, input().split())), reverse=True)
nList = sorted(list(map(int, input().split())), reverse=True)

count = 0
g = 0

for i in range(s):
    if nList[g] > qList[i]:
        count += 1
    else:
        g -= 1
    g += 1
    
print(count)
    