import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(y, x):
    cnt = 0
    visited[y][x] = True
    q = deque([(y,x)])
    while q:
        now = q.popleft()
        cnt += 1
        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and arr[ny][nx] == '1':
                    q.append((ny, nx))
                    visited[ny][nx] = True
    return cnt


n = int(sys.stdin.readline().strip())
arr = []
visited = [[False]*n for _ in range(n)]
total = 0
result = []

for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))
for j in range(n):
    for i in range(n):
        if arr[j][i] == '1' and visited[j][i] == False:
            result.append(bfs(j, i))
            total += 1

print(total)
result.sort()
for i in result:
    print(i)