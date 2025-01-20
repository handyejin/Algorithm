import sys

n, m, v = map(int, sys.stdin.readline().strip().split())
g = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in g[v]:
        if not visited[i]:
            DFS(i)

def BFS(v):
    q = [v]
    visited[v] = True
    while q:
        now = q.pop(0)
        print(now, end=' ')
        for i in g[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)




for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    g[a].append(b)
    g[b].append(a)

for l in g:
    l.sort()

result = []
DFS(v)

visited = [False] * (n+1)
print()
BFS(v)