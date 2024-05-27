import sys

def DFS(v):
    print(v, end=' ')
    global visited
    visited[v] = True

    for next in range(1, n + 1):
        if not visited[next] and graph[v][next]:
            DFS(next)

def BFS(v):
    q = [v]
    visited[v] = True

    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for idx in range(1, n+1):
            if not visited[idx] and graph[cur][idx]:
                visited[idx] = True
                q.append(idx)

n, m, v = map(int, sys.stdin.readline().strip().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = True
    graph[b][a] = True
DFS(v)

print()
visited = [False] * (n + 1)

BFS(v)
