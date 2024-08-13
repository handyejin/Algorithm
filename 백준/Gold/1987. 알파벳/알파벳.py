import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    global answer
    q = set()
    q = {(0, 0, ipt[0][0], 1)}
    visited[0][0] = True

    while q:
        now = q.pop()

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if 0 <= nx < c and 0 <= ny < r:
                if not visited[ny][nx] and ipt[ny][nx] not in now[2]:
                    q.add((nx, ny, now[2] + ipt[ny][nx], now[3] + 1))

        answer = max(answer, now[3])


r, c = map(int, sys.stdin.readline().strip().split())
ipt = []
visited = [[False] * c for _ in range(r)]
answer = 1

for i in range(r):
    ipt.append(list(sys.stdin.readline().strip()))

bfs()
print(answer)
