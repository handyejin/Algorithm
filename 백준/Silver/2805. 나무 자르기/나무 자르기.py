import sys

n, m = map(int, sys.stdin.readline().strip().split())
h = list(map(int, sys.stdin.readline().strip().split()))

answer = 0
start = 0
end = max(h)


while start <= end:
    mid = (start + end) // 2
    s = 0

    for i in h:
        if i - mid > 0:
            s += (i-mid)

    if s >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)
