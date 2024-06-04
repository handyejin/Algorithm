import sys


def backtracking(depth, start):
    if depth == m:
        print(' '.join(answer))
        return

    for i in range(start, n):
        if not visited[i]:
            answer.append(str(arr[i]))
            visited[i] = True
            backtracking(depth + 1, i)
            visited[i] = False
            del answer[-1]


n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
answer = []
visited = [False] * n

arr.sort()
backtracking(0, 0)
