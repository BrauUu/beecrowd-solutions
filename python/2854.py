def dfs(graph, vertex, visited):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

n, m = list(map(int, input().split()))

graph = {}
names = []

for _ in range(m):
    x, _, y = input().split()
    if graph.get(x) == None:
        graph[x] = []
        names.append(x)
    if graph.get(y) == None:
        graph[y] = []
        names.append(y)
        
    graph[x].append(y)
    graph[y].append(x)
    
visited = set()
count = 0
for i in names:
    if i not in visited:
        dfs(graph, i, visited)
        count += 1
print(count)
    
