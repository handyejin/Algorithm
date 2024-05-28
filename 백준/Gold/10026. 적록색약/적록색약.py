import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def BFS(y, x, mode):
    color = graph[y][x]

    while q:
        cur = q.pop(0)
        cur_y = cur[0]
        cur_x = cur[1]

        for i in range(4):
            dy_y = cur_y + dy[i]
            dx_x = cur_x + dx[i]

            if 0 <= dx_x < N and 0 <= dy_y < N:
                if not visited[dy_y][dx_x]:
                    if mode == 0:
                        if graph[dy_y][dx_x] == color:
                            q.append((dy_y, dx_x))
                            visited[dy_y][dx_x] = True
                    elif mode == 1:
                        if color in ('R', 'G'):
                            if graph[dy_y][dx_x] in ('R', 'G'):
                                q.append((dy_y, dx_x))
                                visited[dy_y][dx_x] = True
                        else:
                            if graph[dy_y][dx_x] == color:
                                q.append((dy_y, dx_x))
                                visited[dy_y][dx_x] = True


N = int(sys.stdin.readline())
graph = []
visited = []
for i in range(N):
    graph.append(list(sys.stdin.readline().strip()))
    visited.append([False] * N)

for mode in range(2):
    count = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 0
                q = [(i,j)]
                BFS(i, j, mode)
                count += 1
    print(count, end = ' ')

