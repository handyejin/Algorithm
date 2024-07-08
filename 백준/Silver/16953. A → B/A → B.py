import sys


def dfs(depth, num):
    global B, result
    if num > B:
        return
    elif num == B:
        if result == -1:
            result = depth
        return

    dfs(depth + 1, num * 2)
    dfs(depth + 1, int(str(num) + '1'))


A, B = map(int, sys.stdin.readline().strip().split())
result = -1
dfs(1, A)
print(result)
