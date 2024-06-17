import sys


def valid(answer):
    for i in range(n):
        if sign[i] == '<':
            if answer[i] > answer[i + 1]:
                return False
        elif sign[i] == '>':
            if answer[i] < answer[i + 1]:
                return False
    return True


def backtracking(depth):
    global answer, check, start, end, c, visited

    if depth == n + 1:
        if valid(answer):
            print(answer)
            check = True
        return

    for i in range(start, end, c):
        if not visited[i]:
            visited[i] = True
            answer += str(i)
            backtracking(depth + 1)
            if check:
                visited = [True] * (n+1)
                break
            answer = answer[0: -1]
            visited[i] = False


n = int(sys.stdin.readline().strip())
sign = list(map(str, sys.stdin.readline().strip().split()))

visited = [False] * 10
answer = ''
start = 9
end = -1
c = -1
check = False
backtracking(0)

visited = [False] * 10
answer = ''
check = False
start = 0
end = 10
c = 1
backtracking(0)
