def solution(s):
    answer = True
    arr = []
    
    for x in s:
        if x == "(":
            arr.append(x)
        else:
            if not arr:
                answer = False
                break
            else:     
                arr.pop()
    if len(arr):
        answer = False

    return answer