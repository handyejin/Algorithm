import sys


def bfs(r):
    global cnt
    q = [r]
    visited[r] = cnt
    cnt += 1

    while q:
        now = q.pop(0)

        for x in sorted(graph[now]):
            if visited[x] == 0:
                q.append(x)
                visited[x] = cnt
                cnt += 1


n, m, r = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for _ in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(r)
for i in range(1, n+1):
    print(visited[i])


