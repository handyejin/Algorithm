import sys


def backtracking(depth, start):
    global count

    if depth == m:
        if sum(answer) == S:
            count += 1

    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            answer.append(arr[i])
            backtracking(depth + 1, i)
            visited[i] = False
            del answer[-1]


n, S = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
answer = list()
count = 0
visited = [False] * n

for m in range(1, n+1):
    backtracking(0, 0)

print(count)
