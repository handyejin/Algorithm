import sys

dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]


def bfs(y, x):
    answer = 0
    q = [(y, x, answer)]

    while q:
        now = q.pop(0)
        if now[0] == y2 and now[1] == x2:
            return now[2]

        for i in range(8):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            if 0 <= nx < l and 0 <= ny < l:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx, now[2] + 1))

    return answer


T = int(sys.stdin.readline().strip())

for _ in range(T):
    l = int(sys.stdin.readline().strip())

    visited = [[False] * l for _ in range(l)]

    y1, x1 = map(int, sys.stdin.readline().strip().split())
    y2, x2 = map(int, sys.stdin.readline().strip().split())

    visited[y1][x1] = True
    print(bfs(y1, x1))
