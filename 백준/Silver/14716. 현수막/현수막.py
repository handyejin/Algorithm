# 14716

import sys

dx = [1, 0, -1, 0, -1, 1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]


def bfs(y, x):
    q = list()
    q.append((x, y))

    while q:
        now = q.pop()
        now_x = now[0]
        now_y = now[1]

        for i in range(8):
            dx_x = now_x + dx[i]
            dy_y = now_y + dy[i]

            if 0 <= dx_x < m and 0 <= dy_y < n:
                if not visited[dy_y][dx_x] and arr[dy_y][dx_x] == 1:
                    visited[dy_y][dx_x] = True
                    q.append((dx_x, dy_y))

    return


n, m = map(int, sys.stdin.readline().strip().split())
arr = []
visited = [[False] * m for _ in range(n)]
result = 0

for i in range(n):
    ipt = list(map(int, sys.stdin.readline().strip().split()))
    arr.append(ipt)

for y in range(n):
    for x in range(m):
        if visited[y][x] == 0 and arr[y][x] == 1:
            visited[y][x] = True
            bfs(y, x)
            result += 1

print(result)

