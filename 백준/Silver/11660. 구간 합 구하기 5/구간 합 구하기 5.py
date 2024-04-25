import sys

if __name__ == "__main__":
    n, m = input().split()
    n = int(n)
    m = int(m)

    prefix_sum = [[0 for j in range(n+1)] for i in range(n+1)]
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    results = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + arr[i-1][j-1] - prefix_sum[i-1][j-1]

    for i in range(m):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

        results.append(prefix_sum[x2][y2] - prefix_sum[x1-1][y2] -prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1])

    for result in results:
        print(result)