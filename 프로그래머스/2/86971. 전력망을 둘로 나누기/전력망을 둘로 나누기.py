from collections import deque

def bfs(num1, num2):
    global graph, visited
    count = 1
    q = deque()
    q.append(num1)
    visited[num1] = True
    
    while q:
        now = q.pop()
        for n in graph[now]:
            if not visited[n] and n != num2:
                q.append(n)
                count += 1
                visited[n] = True
    return count
    

def solution(n, wires):
    global graph, visited
    answer = 100000
    graph = [[] for _ in range(n+1)]
    
    for l in wires:
        graph[l[0]].append(l[1])
        graph[l[1]].append(l[0])
        
    for w in wires:
        visited = [False] * (n+1)
        c1 = bfs(w[0], w[1])
        visited = [False] * (n+1)
        c2 = bfs(w[1], w[0])
                
        answer = min(answer, abs(c1-c2))
                
    return answer