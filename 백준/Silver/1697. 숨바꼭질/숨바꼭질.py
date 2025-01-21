import sys

def bfs():
    q = [(n, 0)]

    while q:
        now = q.pop(0)
        if now[0] == k:
            return now[1]

        if 0<= (now[0]*2) <= 100000 and now[0]*2 not in visited:
            q.append((now[0]*2, now[1]+1))
            visited.add((now[0]*2))
        if 0<= (now[0]+1) <= 100000 and now[0]+1 not in visited:
            q.append((now[0]+1, now[1]+1))
            visited.add(now[0]+1)
        if 0<= (now[0]-1) <= 100000 and now[0]-1 not in visited:
            q.append((now[0]-1, now[1]+1))
            visited.add(now[0]-1)


n, k = map(int, sys.stdin.readline().strip().split())
visited = set()
print(bfs())