# 21736

import sys


def bfs(y, x):
    global result
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = list()
    q.append((x, y))

    while q:
        now = q.pop()
        if arr[now[1]][now[0]] == 'P':
            result += 1
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and arr[ny][nx] != 'X':
                    visited[ny][nx] = True
                    q.append((nx, ny))


n, m = map(int, sys.stdin.readline().strip().split())
arr = []
visited = [[False] * m for _ in range(n)]
result = 0
for i in range(n):
    ipt = list(sys.stdin.readline().strip())
    arr.append(ipt)


for y in range(n):
    for x in range(m):
        if arr[y][x] == 'I':
            visited[y][x] = True
            bfs(y, x)
            break

if result > 0:
    print(result)
else:
    print('TT')
