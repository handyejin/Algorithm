import sys

arr = list()

answer = []


def Backtracking(depth, arr):
    if depth == M + 1:
        s = ' '.join(arr)
        print(s)

        return
    for i in range(1, N+1):

        arr.append(str(i))
        Backtracking(depth + 1, arr)
        del arr[-1]


N, M = map(int, sys.stdin.readline().strip().split())
Backtracking(1, [])
