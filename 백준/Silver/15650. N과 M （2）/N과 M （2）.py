import sys


def backtracking(depth, start):
    global visited, level
    if depth == m:
        print(' '.join(arr))
        return

    for i in range(start, n + 1):
        if not visited[i]:
            arr.append(str(i))
            visited[i] = True
            backtracking(depth + 1, i+1)
            visited[i] = False
            del arr[-1]


n, m = map(int, sys.stdin.readline().strip().split())
level = 0
arr = []
visited = [False] * (n + 1)

backtracking(0, 1)
