import sys

n = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().strip().split()))
lst.insert(0, 0)

dp = [0] * (n+1)

for i in range(n+1):
    mx = 0
    for j in range(i):
        if lst[i] > lst[j]:
            mx = max(mx, dp[j])

        dp[i] = mx + lst[i]

print(max(dp))