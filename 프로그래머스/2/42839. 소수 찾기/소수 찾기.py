import math

def dfs(depth, numbers, s):
    global visited, result_set, answer
    if depth > len(numbers):
        return
    else:
        # 소수 검사
        print(s)
        if s:
            num = int(s)
            is_prime = True
            if num not in result_set:
                # print(num)
                result_set.add(num)
                if num in (0, 1):
                    is_prime = False
                else:
                    for i in range(2, int(num**0.5) + 1):
                        if num % i == 0:
                            # print(num, i)
                            is_prime = False
                            break
                if is_prime:
                    answer += 1
                
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            s+=numbers[i]
            dfs(depth+1, numbers, s)
            visited[i] = False
            s = s[0: -1]

def solution(numbers):
    global result_set , visited, answer
    answer = 0
    result_set = set()
    visited = [False] * len(numbers)
    dfs(0, numbers, '')
    
    return answer