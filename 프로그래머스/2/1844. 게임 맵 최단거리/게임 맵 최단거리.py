
def solution(maps):
    answer = -1
    row = len(maps)
    col = len(maps[0])
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    q = [(0, 0, 1)]
    visited = [[False] * col for _ in range(row)]
    while q:
        now = q.pop(0)
        if now[0] == row-1 and now[1] == col-1:
            answer = now[2]
            break
        
        for i in range(4):
            cx = now[1] + dx[i]
            cy = now[0] + dy[i]
            
            if 0 <= cx < col and 0 <= cy < row:       
                if not visited[cy][cx] and maps[cy][cx] == 1:
                    q.append((cy, cx, now[2] + 1))
                    visited[cy][cx] = True
    return answer