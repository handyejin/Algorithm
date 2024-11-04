import sys


def bfs(node):
    q = [(node, 0)]
    visited[node] = True

    while q:
        now = q.pop(0)

        if now[0] == b:
            return now[1]

        for i in graph[now[0]]:
            if not visited[i]:
                visited[i] = True
                q.append((i, now[1] + 1))
    return -1


n = int(sys.stdin.readline().strip())

a, b = map(int, sys.stdin.readline().strip().split())

m = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
for _ in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(a))
