import sys


def get_cnt(mid):
    cnt = 0
    for num in l:
        cnt += num // mid
    return cnt

k, n = map(int, sys.stdin.readline().strip().split())
l = list()
for _ in range(k):
    l.append(int(sys.stdin.readline().strip()))

start = 1
end = max(l)
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = get_cnt(mid)

    if cnt < n:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)