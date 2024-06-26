import sys


def dfs(depth):
    if depth == k:
        anw = ''.join(str(x) for x in result)
        if anw not in result_set:
            result_set.add(anw)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])
            dfs(depth + 1)
            visited[i] = False
            del result[-1]


n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
arr = list()
result_set = set()
result = []
visited = [False] * n

for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

dfs(0)
print(len(result_set))
