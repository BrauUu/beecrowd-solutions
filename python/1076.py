def dfs(graph, v):
    vFound = [v]
    vVisited = []
    count = 0
    while len(vFound) > 0:
        vertice = vFound.pop()
        vVisited.append(vertice)
        edges = graph[vertice]
        for edge in edges:
            if vVisited.count(edge) == 0 and vFound.count(edge) == 0:
                vFound.append(edge)
        count += 1

    return (count-1) * 2



t = int(input())

for _ in range(t):
    n = int(input())
    v, a = list(map(int, input().split()))
    graph = [[] for i in range(v)]
    for _ in range(a):
        v1, v2 = list(map(int, input().split()))
        if graph[v1].count(v2) == 0:
            graph[v1].append(v2)
            graph[v2].append(v1)
    print(dfs(graph=graph, v=n))