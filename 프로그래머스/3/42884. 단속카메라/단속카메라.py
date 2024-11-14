
def solution(routes):
    answer = 0
    sorted_r = sorted(routes, key=lambda x: x[1])
    # print(sorted_r)

    l = -30000
    
    for sr in sorted_r:
        if sr[0] <= l <= sr[1]:
            pass
        else:
            answer += 1
            l = sr[1]
        
    
    return answer