# N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.
import sys

def dfs(depth):
    if depth == n:
        print(' '.join(x for x in result))
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(str(i))
            dfs(depth+1)
            del result[-1]
            visited[i] = False


n = int(sys.stdin.readline().strip())

result = []
visited = [False] * (n+1)
dfs(0)
