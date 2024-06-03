import sys

arr = []


def backtraking(depth):
    if depth == m:
        print(' '.join(arr))
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            arr.append(str(i))

            backtraking(depth + 1)

            visited[i] = False
            del arr[-1]


n, m = map(int, sys.stdin.readline().strip().split())
visited = [False] * (n+1)
backtraking(0)
