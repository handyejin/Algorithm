import sys


def backtracking(depth, start):
    if depth == m:
        print(' '.join(answer))
        return

    for i in range(start, n):
        answer.append(str(arr[i]))
        backtracking(depth + 1, i)
        del answer[-1]


n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
answer = []

arr.sort()
backtracking(0, 0)
