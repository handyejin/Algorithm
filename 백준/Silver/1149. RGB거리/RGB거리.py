import sys
sys.setrecursionlimit(10**6)

def dfs(depth, idx):
    global Min

    if depth == n:
        return 0
    if dp[depth][idx] != sys.maxsize:
        return dp[depth][idx]

    for i in range(1, 4):
        if i != idx:
            dp[depth][idx] = min(dfs(depth + 1, i) + arr[depth][i-1], dp[depth][idx])

    return dp[depth][idx]


n = int(sys.stdin.readline().strip())
s = 0
result = []
arr = []
dp = [[sys.maxsize] * 4 for _ in range(n+1)]
Min = sys.maxsize

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

print(dfs(0, 0))

