def check_count(k, dungeons):
    global arr, answer
    ck = k
    count = 0
    for i in arr:
        if ck >= dungeons[i][0]:
            ck -= dungeons[i][1]
            count +=1
        else:
            break
    return count
    
def dfs(depth, dungeons, k):
    global arr, n, answer, visited
    if depth == n:
        answer = max(answer, check_count(k, dungeons))
        return
        
    for i in range(n):
        if not visited[i] :
            visited[i] = True
            arr.append(i)
            dfs(depth+1, dungeons, k)
            del arr[-1]
            visited[i] = False
        

def solution(k, dungeons):
    global arr, n, visited, answer
    arr = list()
    n = len(dungeons)
    visited = [False] * n
    answer = -1
    dfs(0, dungeons, k)
    return answer