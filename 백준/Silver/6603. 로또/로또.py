import sys


def backtracking(depth, start):
    if depth == 6:
        print(' '.join(answer))
        return

    for i in range(start, k):
        if not visited[i]:
            visited[i] = True
            answer.append(str(arr[i]))
            backtracking(depth + 1, i)
            visited[i] = False
            del answer[-1]


while True:
    arr = list(map(int, sys.stdin.readline().strip().split()))
    k = arr.pop(0)

    if k == 0:
        break

    visited = [False] * k
    answer = []
    arr.sort()

    backtracking(0, 0)
    print()
