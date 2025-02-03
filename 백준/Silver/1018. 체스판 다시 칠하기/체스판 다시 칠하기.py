import sys

n, m = map(int, sys.stdin.readline().strip().split())
x, y = 0, 0
arr = []
Min = 2500

for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))

for k in range(n-7):
    for x in range(m-7):
        cnt = 0
        for i in range(k, k+8):
            for j in range(x, x+8):
                # W인 경우 먼저 구하기
                if (i+j) % 2 == 0:
                    if arr[i][j] == 'B':
                        cnt += 1
                else:
                    if arr[i][j] == 'W':
                        cnt += 1

        Min = min(Min, cnt, 64 - cnt)

print(Min)