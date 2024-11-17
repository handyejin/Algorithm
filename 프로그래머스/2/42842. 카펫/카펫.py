def divisor(n):
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n %  i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(d)
            
    

def solution(brown, yellow):
    answer = []
    x = 0
    y = 0
    
    tmp = brown + yellow
    d = divisor(tmp)
    print(d)
    
    start = 0
    end = len(d) - 1
    
    while start <= end:
        if d[start] * d[end] == tmp:
            if (d[start]-2)*(d[end] - 2) == yellow:
                answer.append(d[end])
                answer.append(d[start])
        
                break
        start += 1
        end -= 1
    
    return answer