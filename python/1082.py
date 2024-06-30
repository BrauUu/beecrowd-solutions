def dfs(graph, vertex, visited, component):
    component.append(vertex)
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)

n = int(input())
for i in range(n):
    v, e = list(map(int, input().split()))
    unicodeInitialValue = 97
    graph = {chr(i) : [] for i in range(unicodeInitialValue, unicodeInitialValue + v)}
    for _ in range(e):
        v1, v2 = input().split()
        graph[v1].append(v2)
        graph[v2].append(v1)
    visited = set()
    components = []
    for vertex in graph:
        if vertex not in visited:
            component = []
            dfs(graph=graph, vertex=vertex, visited=visited, component=component)
            component.sort()
            components.append(component)
    print(f'Case #{i + 1}:')
    for component in components:
        print(*component, sep=',', end=',\n')
    print(f'{len(components)} connected components\n')