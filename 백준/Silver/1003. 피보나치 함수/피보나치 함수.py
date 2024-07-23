import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    ipt = int(sys.stdin.readline().strip())

    dp = [tuple()] * (ipt + 1)
    dp[0] = (1, 0)
    if ipt > 0:
        dp[1] = (0, 1)

        for i in range(2, ipt+1):
            dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
    print(' '.join(str(s) for s in dp[ipt]))