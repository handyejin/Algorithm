"""
5 5 1
1 4
1 2
2 3
2 4
3 4

"""

import sys
sys.setrecursionlimit(10 ** 6)


def dfs(r, depth):
    global cnt

    visited[r] = cnt
    for i in sorted(graph[r]):
        if visited[i] == 0:
            cnt += 1
            dfs(i, depth + 1)


cnt = 1
n, m, r = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(r, 1)
visited[r] = 1

for i in range(1, n+1):
    print(visited[i])