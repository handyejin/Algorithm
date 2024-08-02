def solution(answers):
    answer = []
    l = len(answers)
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]  
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    [1, 3, 4, 2, 5, 5, 3, 1, 2, 3, 4, 1, 2, 3, 1, 1, 1, 5]
    
    result = {1: 0, 2: 0, 3: 0}
    
    max = -1
        
    for i in range(len(answers)):
        if answers[i] == a1[i%5]:
            result[1] += 1
        if answers[i] == a2[i%8]:
            result[2] += 1
        if answers[i] == a3[i%10]:
            result[3] += 1
                    
    for key, value in result.items():
        if value > max:
            max = value
            answer = []
            answer.append(key)
        elif value == max:
            answer.append(key)
    answer.sort() 
    
    return answer