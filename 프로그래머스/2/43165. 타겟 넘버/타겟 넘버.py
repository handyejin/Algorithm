def cal(s, numbers, target):
    global answer
    result = 0
    for i in range(len(numbers)):
        if s[i] == '-':
            result += numbers[i] * -1
        else:
            result += numbers[i]
    
    if result == target:
        answer += 1
            
def dfs(depth, numbers, target, s):
    if depth == len(numbers):
        cal(s, numbers, target)
        return
        
    dfs(depth + 1, numbers, target, s+'+')
    dfs(depth + 1, numbers, target, s+'-')    

def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, numbers, target, '')
    return answer