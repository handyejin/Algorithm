import sys

sys.setrecursionlimit(10 ** 6)


def backtracking(depth, s, cnt):
    global count

    if depth == n:
        if cnt > 0 and s == S:
            count += 1
        return

    # 포함할 경우
    backtracking(depth + 1, s + arr[depth], cnt+1)

    # 포함하지 않을 경우
    backtracking(depth + 1, s, cnt)


n, S = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
count = 0

backtracking(0, 0, 0)
print(count)
