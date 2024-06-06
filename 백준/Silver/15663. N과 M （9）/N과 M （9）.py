import sys


def backtracking(depth):
    if depth == m:
        result_str = ' '.join(answer)
        if result_str not in result:
            print(result_str)
            result.add(result_str)
        return

    for i in range(0, n):
        if not visited[i]:
            answer.append(str(arr[i]))
            visited[i] = True
            backtracking(depth + 1)
            visited[i] = False
            del answer[-1]


n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
visited = [False] * n
answer = []
answer_list = list()
result = []
result = set(result)

arr.sort()
backtracking(0)

