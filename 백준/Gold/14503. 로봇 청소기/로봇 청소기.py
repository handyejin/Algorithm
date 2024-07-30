import sys

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(y, x, d):
    global result

    while True:
        if arr[y][x] == '0' and not visited[y][x]:
            visited[y][x] = True
            result += 1
        is_blink = True
        for i in range(4):
            if arr[y + dy[i]][x + dx[i]] == '0' and not visited[y + dy[i]][x + dx[i]]:
                is_blink = False

        # 청소되지 않은 빈칸이 있는 경우
        if not is_blink:
            # 90도 회전
            d = 3 if d == 0 else d - 1
            ny = y + dy[d]
            nx = x + dx[d]

            if not visited[ny][nx] and arr[ny][nx] == '0':
                y = ny
                x = nx
        else:
            ny = y - dy[d]
            nx = x - dx[d]

            if arr[ny][nx] == '1':
                break
            else:
                y = ny
                x = nx


n, m = map(int, sys.stdin.readline().strip().split())
r, c, d = map(int, sys.stdin.readline().strip().split())
arr = []
visited = [[False] * m for _ in range(n)]
result = 0

for _ in range(n):
    arr.append(list(sys.stdin.readline().strip().split()))

bfs(r, c, d)
print(result)