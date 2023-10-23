n, m = list(map(int, input().split()))

map = []

for i in range(n):
    map.append(input())
    
count = 0
for i in range(n):
    c = 0
    while True:
            c = map[i].find('#', c)
            if c == -1:
                break
            elif i == 0 or i == n - 1 or c == m - 1 or c == 0:
                count += 1
            elif map[i][c+1] == '.' or map[i][c-1] == '.' or map[i-1][c] == '.' or map[i+1][c] == '.':
                count += 1
            c += 1

print(count)