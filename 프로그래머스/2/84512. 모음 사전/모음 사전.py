def dfs(depth, word):
    global result, answer, cnt
    
    if ''.join(result) == word:
        answer = cnt
        return

    if depth == 5:
        return
    
    for w in ('A', 'E', 'I', 'O', 'U'):
        result.append(w)
        cnt += 1
        dfs(depth+1, word)
        del result[-1]

        
        

def solution(word):
    global result, answer, cnt
    result = []
    answer = 0
    cnt = 0
    dfs(0, word)
    return answer
