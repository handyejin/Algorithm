import sys
from collections import deque

dv = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]


def bfs():
    global q
    day = 0
    while q:
        now = q.popleft()
        if day < now[3]:
            day = now[3]
        for i in range(6):
            nh = now[0] + dv[i]
            ny = now[1] + dy[i]
            nx = now[2] + dx[i]

            if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M:
                if not visited[nh][ny][nx] and graph[nh][ny][nx] == 0:
                    q.append((nh, ny, nx, now[3] + 1))
                    visited[nh][ny][nx] = True
                    graph[nh][ny][nx] = now[3] + 1

    return day


M, N, H = map(int, sys.stdin.readline().strip().split())
graph = []
answer = 0
status = True
q = deque()

for _ in range(H):
    g = []
    for _ in range(N):
        g.append(list(map(int, sys.stdin.readline().strip().split())))
    graph.append(g)

visited = [[[False] * M for _ in range(N)] for _ in range(H)]

for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 1:
                q.append((k, i, j, 0))
                visited[k][i][j] = True

answer = bfs()

for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 0:
                status = False

if status:
    print(answer)
else:
    print(-1)
