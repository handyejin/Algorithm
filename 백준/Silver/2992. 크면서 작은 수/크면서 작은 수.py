import sys


def dfs(depth):
    global result
    if depth == len(L):
        num = int(''.join(str(x) for x in answer))
        if result == 0 and num > ipt:
            result = num
            return
    for i in range(len(L)):
        if not visited[i]:
            visited[i] = True
            answer.append(L[i])
            dfs(depth + 1)
            del answer[-1]
            visited[i] = False


ipt = int(sys.stdin.readline().strip())
L = list(str(ipt))
L.sort()
result = 0
visited = [False] * len(L)
answer = []

dfs(0)
print(result)
