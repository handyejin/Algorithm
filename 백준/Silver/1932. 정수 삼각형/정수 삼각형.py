# 1932
import sys

def dfs(depth, idx):
    global dp

    if depth == n:
        return dp[depth][idx]

    if dp[depth][idx] == 0:
        dp[depth][idx] = max(dfs(depth+1, idx), dfs(depth+1, idx+1)) + t[depth][idx]
    return dp[depth][idx]

    # dfs(depth + 1, index + 1, Sum + t[depth][index])


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    t = list()
    Max = 0
    result_set = set()
    dp = [[0]*(n+1) for _ in range(n+1)]

    for _ in range(n):
        ipt = list(map(int, sys.stdin.readline().strip().split()))
        t.append(ipt)

    # depth, index, answer
    print(dfs(0, 0))