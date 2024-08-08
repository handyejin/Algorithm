def dfs(depth, word):
    global answer, result, count
    if word == result:
        answer = count
        return
    
    if depth == 5:
        return
    
        
    for s in ['A', 'E', 'I', 'O', 'U']:
        result += s
        count += 1
        dfs(depth +1, word)
        result = result[0:-1]
        

def solution(word):
    global result, answer, count
    answer = 0
    result = ''
    count = 0
    dfs(0, word)
    return answer