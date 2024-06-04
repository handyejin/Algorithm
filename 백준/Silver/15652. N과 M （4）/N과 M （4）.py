import sys


def backtracking(depth, start):
    if depth == m:
        print(' '.join(arr))
        return

    for i in range(start, n + 1):
        arr.append(str(i))
        backtracking(depth + 1, i)
        del arr[-1]


arr = list()
n, m = map(int, sys.stdin.readline().strip().split())
backtracking(0, 1)
