import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = []

def DFS(y, x):
    global visited
    visited[y][x] = True

    for i in range(4):
        cur_y = y + dy[i]
        cur_x = x + dx[i]

        if 0 <= cur_x < M and 0 <= cur_y < N:
            if not visited[cur_y][cur_x] and graph[cur_y][cur_x]:
                DFS(cur_y, cur_x)


for _ in range(T):
    count = 0
    M, N, K = map(int, sys.stdin.readline().strip().split())
    graph = [[False] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for k in range(K):
        x, y = map(int, sys.stdin.readline().strip().split())
        graph[y][x] = True

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1:
                DFS(i, j)
                count += 1
    result.append(count)

for r in result:
    print(r)

