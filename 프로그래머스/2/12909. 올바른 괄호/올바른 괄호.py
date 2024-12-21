def solution(s):
    answer = True
    st = []
    
    for x in s:
        if x == "(":
            st.append(x)
        else:
            if st:
                st.pop()
            else:
                answer = False
    if st:
        answer = False
    


    return answer