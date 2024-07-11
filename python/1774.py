class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    s = 0

    for u, v, weight in edges:
        if uf.find(u-1) != uf.find(v-1):
            uf.union(u-1, v-1)
            mst.append((u, v, weight))
            s += weight
            
    return s


r, c = list(map(int, input().split()))

graph = []

for _ in range(c):
    v, w, p = list(map(int, input().split()))
    graph.append((v, w, p))
s = kruskal(r, graph)
print(s)