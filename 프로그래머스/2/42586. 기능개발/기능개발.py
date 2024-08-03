import math

def solution(progresses, speeds):
    answer = []
    q = []
    count = 1
    for i in range(len(progresses)):
        q.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    before = q.pop(0)
    while q:
        now = q.pop(0)
        print(before, now)
        if now > before:
            answer.append(count)
            count = 1
            before = now
        else:
            count += 1
    answer.append(count)
    return answer