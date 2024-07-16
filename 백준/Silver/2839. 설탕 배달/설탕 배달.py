import sys

num = int(sys.stdin.readline().strip())
dp = [5000] * (num+1)

dp[3] = 1
if num >= 5:
    dp[5] = 1

for i in range(6, num+1):
    dp[i] = min(dp[i-5], dp[i-3]) + 1


if dp[num] >= 5000:
    print(-1)
else:
    print(dp[num])

