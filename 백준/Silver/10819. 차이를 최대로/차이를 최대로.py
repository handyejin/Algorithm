import sys


def cal(arr):
    S = 0
    for i in range(2, N + 1):
        S += abs(arr[i - 2] - arr[i - 1])
    return S


def backtracking(depth):
    global answer, Max
    if depth == N:
        s_answer = ' '.join(str(x) for x in answer)
        if s_answer not in result_set:
            result_set.add(s_answer)
            S = cal(answer)
            Max = max(S, Max)
        return

    for i in range(0, N):
        if not visited[i]:
            visited[i] = True
            answer.append(A[i])
            backtracking(depth + 1)
            del answer[-1]
            visited[i] = False


N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

answer = list()
result_set = set()
Max = -1 * sys.maxsize -1
visited = [False] * N
backtracking(0)

print(Max)
