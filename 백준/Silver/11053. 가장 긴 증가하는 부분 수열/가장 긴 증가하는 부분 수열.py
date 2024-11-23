import sys

n = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().strip().split()))
lst.insert(0, 0)
dp = [0] * (n+1)


for i in range(len(lst)):
    mx = 0
    for j in range(i):
        if lst[i] > lst[j]:
            mx = max(dp[j], mx)

        dp[i] = mx + 1

print(max(dp))
