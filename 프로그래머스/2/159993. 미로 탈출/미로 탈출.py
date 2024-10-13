dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(maps, start, end):
    global m, n
    
    answer = -1
    visited = [[False] * m for _ in range(n)]    
    q = []
    q.append((start[0], start[1], 0))    
    visited[start[0]][start[1]] = True
    
    while q:
        now = q.pop(0)
        if now[0] == end[0] and now[1] == end[1]:
            answer = now[2]
            break
        
        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and maps[ny][nx] != 'X':
                    visited[ny][nx] = True
                    q.append((ny, nx, now[2]+1))
    return answer
    
def solution(maps):
    global m, n
    
    n =len(maps)
    m = len(maps[0])
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                l = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)
                
    l_count = bfs(maps, start, l)
    e_count = bfs(maps, l, exit)
    
    if l_count == -1 or e_count == -1:
        return -1
    else:
        return l_count+ e_count
    
    