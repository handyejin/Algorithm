import sys

n = int(sys.stdin.readline().strip())
result_set = set()
# (0, 1) 개수
cnt = [0, 1]
if n == 1:
    print(1)
else:
    for _ in range(n-1):
        total = cnt[0] + cnt[1]
        cnt[1] = cnt[0]
        cnt[0] = total

    print(cnt[0] + cnt[1])