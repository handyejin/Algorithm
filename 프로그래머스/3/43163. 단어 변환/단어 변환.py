def check(word, target):
    
    cnt = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            cnt += 1
            
    if cnt == 1:
        # print(word, target)
        return True
    else:
        return False
        

def dfs(depth, word, target, words, count):
    global answer
    if depth == len(words):
        return
    if check(word, target):
        answer = count
        return count
    
    for i in range(len(word)):
        if check(word, words[i]) and words[i] not in answers:
            answers.append(words[i])
            dfs(depth+1, words[i], target, words, count+1)
            answers.pop()
    
        
def solution(begin, target, words):
    global answer,  answers
    answer = 0
    answers = []
    if target in words:
        dfs(0, begin, target, words, 1)
    
    
    return answer