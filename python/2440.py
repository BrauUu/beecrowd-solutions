import sys

sys.setrecursionlimit(50000) 

def dfs(graph, vertex, visited):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

n, m = list(map(int, input().split()))

graph = {i: [] for i in range(1, n + 1)}

for i in range(m):
    x1, x2 = list(map(int, input().split()))
    graph[x1].append(x2)
    graph[x2].append(x1)
    
visited = set()
count = 0
for i in range(1, n + 1):
    if i not in visited:
        dfs(graph, i, visited)
        count += 1
print(count)
            
