def solution(n, times):
    answer = 0
    start = 0
    end = max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        print(start, mid, end)
        tmp = 0
        for t in times:
            tmp += mid // t
        
        if tmp >= n:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
            
    return answer