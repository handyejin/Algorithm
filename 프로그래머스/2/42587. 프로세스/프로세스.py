def solution(priorities, location):
    answer = 0
    pq = []
    
    
    for i in range(len(priorities)):
        pq.append((priorities[i], i))
    
    while pq:
        check = True
        value = pq.pop(0)

        print(value)

        for i in range(len(pq)):
            if value[0] < pq[i][0]:
                pq.append(value)
                check = False
                break 
                
        if check:
            answer += 1  
            if value[1] == location:
                break

    return answer