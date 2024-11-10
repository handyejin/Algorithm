import sys

n = int(sys.stdin.readline().strip())
x =  n // 5
cnt = 0


for i in range(x, -1, -1):
    if (n - 5 * i) % 2 == 0:
        cnt += i
        cnt += (n - 5*i) // 2
        break
    else:
        continue

if cnt == 0:
    print(-1)
else:
    print(cnt)

