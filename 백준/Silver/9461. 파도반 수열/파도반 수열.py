import sys

t = int(sys.stdin.readline().strip())
lst = []
for _ in range(t):
    lst.append(int(sys.stdin.readline().strip()))

n = max(lst)

dp = [0] * (n+1)
dp[1] = 1
dp[2] = 1

for i in range(3, n+1):
    dp[i] = dp[i-3] + dp[i-2]

for i in lst:
    print(dp[i])