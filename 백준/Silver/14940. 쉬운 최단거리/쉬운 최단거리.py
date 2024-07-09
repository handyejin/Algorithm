import sys

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    q = [(x, y, 0)]
    visited[y][x] = True

    while q:
        cur = q.pop(0)
        result[cur[1]][cur[0]] = cur[2]

        for k in range(4):
            nx = cur[0] + dx[k]
            ny = cur[1] + dy[k]

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and arr[ny][nx] == '1':
                    visited[ny][nx] = True
                    q.append((nx, ny, cur[2] + 1))


n, m = map(int, sys.stdin.readline().strip().split())

arr = []
result = []
tar_x = 0
tar_y = 0

for i in range(n):
    ipt = list(sys.stdin.readline().strip().split())
    tmp = [0] * m
    for j in range(m):
        if '1' in ipt[j]:
            tmp[j] = -1
        elif '2' in ipt[j]:
            tar_x = j
            tar_y = i

    arr.append(ipt)
    result.append(tmp)

visited = [[False] * m for _ in range(n)]
bfs(tar_x, tar_y)
for i in range(n):
    print(' '.join(str(x) for x in result[i]))
