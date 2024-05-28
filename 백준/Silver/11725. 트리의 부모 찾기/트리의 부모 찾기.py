import sys

sys.setrecursionlimit(10 ** 6)


def DFS(v):
    global visited
    for idx in graph[v]:
        if visited[idx] == 0:
            visited[idx] = v
            DFS(idx)


N = int(sys.stdin.readline().strip())

graph = [[] for _ in range(N+1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())

    graph[a].append(b)
    graph[b].append(a)

visited[0] = 1
visited[1] = 1
DFS(1)

for i in range(2, N + 1):
    print(visited[i])
