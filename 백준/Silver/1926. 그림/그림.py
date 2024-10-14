import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(y, x):
    answer = 1
    q = [(y, x)]

    while q:
        now = q.pop()
        for k in range(4):
            ny = now[0] + dy[k]
            nx = now[1] + dx[k]

            if 0 <= nx < m and 0 <= ny < n:
                if ipt[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    answer += 1
                    q.append((ny, nx))
    return answer


n, m = map(int, sys.stdin.readline().strip().split())
ipt = []
c = 0
M = 0

for i in range(n):
    ipt.append(list(map(int, sys.stdin.readline().strip().split())))

visited = [[False] * m for _ in range(n)]


for i in range(n):
    for j in range(m):
        if ipt[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            result = bfs(i, j)
            M = max(result, M)
            c += 1


print(c)
print(M)