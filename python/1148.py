from sys import maxsize, stdin, stdout
import heapq

def dijkstra(graph, start):
    nVertex = len(graph)
    distances = [maxsize] * nVertex
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        dist, u = heapq.heappop(heap)
        if dist > distances[u]:
            continue
        for v, weight in enumerate(graph[u]):
            if weight == 0:
                continue
            alt = dist + (weight if graph[v][u] == 0 else 0)
            if alt < distances[v]:
                distances[v] = alt 
                heapq.heappush(heap, (alt, v))

    return distances

# while True:
#     n, e = map(int, stdin.readline().split())
#     if n == e == 0:
#         break

#     graph = [[0 for _ in range(n)] for _ in range(n)]

#     for _ in range(e):
#         x, y, h = map(int, stdin.readline().split())
#         graph[x-1][y-1] = h

#     k = int(stdin.readline())
#     distances = []

#     for i in range(n):
#         distances.append(dijkstra(graph, i))

#     for _ in range(k):
#         o, d = map(int, stdin.readline().split())
#         dres = distances[o-1][d-1]
#         stdout.write(f'{dres if dres != maxsize else "Nao e possivel entregar a carta"}\n')
#     stdout.write('\n')

while True:
    n, e = list(map(int, stdin.readline().split()))
    if n == e == 0:
        break

    graph = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(e):
        x, y, h = list(map(int, stdin.readline().split()))
        graph[x-1][y-1] = h

    k = int(stdin.readline())
    distances = [[]] * n

    for _ in range(k):
        o, d = list(map(int, stdin.readline().split()))
        o -= 1
        d -= 1
        if len(distances[o]) == 0:
            distances[o] = dijkstra(graph, o)
        dres = distances[o][d]
        stdout.write(f'{dres if dres != maxsize else "Nao e possivel entregar a carta"}\n')
    stdout.write('\n')