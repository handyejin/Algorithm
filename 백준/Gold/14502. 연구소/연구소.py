import sys

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(y, x):
    q = [(y, x)]
    count = 0
    while q:
        count += 1
        now = q.pop(0)
        for i in range(4):
            cx = now[1] + dx[i]
            cy = now[0] + dy[i]

            if 0 <= cx < m and 0 <= cy < n:
                if not bfs_visited[cy][cx] and arr[cy][cx] == '0' and (cy, cx) not in wall_list:
                    # print(cy, cx)
                    q.append((cy, cx))
                    bfs_visited[cy][cx] = True
    return count


def dfs(depth, sy, sx):
    global result, bfs_visited
    if depth == 3:
        count = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in wall_list and arr[i][j] == '2':
                    if not bfs_visited[i][j]:
                        # print(wall_list, i, j)
                        bfs(i, j)

        for i in range(n):
            for j in range(m):
                if (i, j) not in wall_list and not bfs_visited[i][j] and arr[i][j] == '0':
                    count += 1
        result = max(result, count)
        bfs_visited = [[False] * m for _ in range(n)]
        return

    for i in range(sy, n):
        if i == sy:
            sx2 = sx
        else:
            sx2 = 0

        for j in range(sx2, m):
            if not visited[i][j] and arr[i][j] == '0':
                visited[i][j] = True
                wall_list.append((i, j))
                dfs(depth + 1, i, j)
                del wall_list[-1]
                visited[i][j] = False


n, m = map(int, sys.stdin.readline().strip().split())
arr = [] * n
visited = [[False] * m for _ in range(n)]
bfs_visited = [[False] * m for _ in range(n)]
wall_list = []
result = -1

for i in range(n):
    arr.append(list(sys.stdin.readline().split()))

dfs(0, 0, 0)
print(result)
