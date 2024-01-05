n, t = list(map(int, input().split()))

l = []
teams = [[] for _ in range(t)]

for _ in range(n):
    name, ab = input().split()
    l.append((name, int(ab)))
    
l = sorted(l, key=lambda x: x[1], reverse=True)

for i in range(n):
    teams[i%t].append(l[i][0])

for i in range(t):
    teams[i].sort()
    
for i in range(t):
    print(f'Time {i+1}')
    print(*teams[i], sep='\n')
    print()