import sys


def dfs(depth, start):
    global m, result, visited
    if depth == m:
        s = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] == '1':
                    diff = []
                    for yx in chicken_xy:
                        diff.append((abs(yx[0] - i) + abs(yx[1] - j)))
                    s += min(diff)

        result = min(result, s)
        return

    sy = start[0]
    sx = start[1]

    for y in range(sy, n):
        for x in range(sx, n):

            if not visited[y][x] and arr[y][x] == '2':
                chicken_xy.append((y, x))
                visited[y][x] = True
                dfs(depth + 1, (y, x))
                del chicken_xy[-1]
                visited[y][x] = False
            sx = 0


n, m = map(int, sys.stdin.readline().strip().split())

arr = []
chicken_xy = []
result = 1e9
for _ in range(n):
    arr.append(list(sys.stdin.readline().strip().split()))
visited = [[False]*n for _ in range(n)]


dfs(0, (0, 0))
print(result)
