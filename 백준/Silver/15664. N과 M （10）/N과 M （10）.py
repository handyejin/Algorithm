import sys


def backtracking(depth, start):
    if depth == m:
        answer_str = ' '.join(answer)
        if answer_str not in result:
            result.add(answer_str)
            print(answer_str)

    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            answer.append(str(arr[i]))
            backtracking(depth + 1, i)
            visited[i] = False
            del answer[-1]


n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
visited = [False] * n
answer = []
result = set()
arr.sort()
backtracking(0, 0)
