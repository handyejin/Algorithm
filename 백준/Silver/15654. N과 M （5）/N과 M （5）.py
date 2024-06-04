import sys


def backtracking(depth):
    if depth == m:
        print(' '.join(answer))
        return

    for i in range(0, n):
        if not visited[i]:
            visited[i] = True
            answer.append(str(arr[i]))
            backtracking(depth + 1)

            del answer[-1]
            visited[i] = False


n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
answer = []
visited = [False] * n

arr.sort()
backtracking(0)
