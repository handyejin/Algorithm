import sys

def get_cnt_a(num):
    start = 0
    end = n - 1
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if l[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return start

def get_cnt_b(num):
    start = 0
    end = n - 1
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if l[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return start -1




n, m = map(int, sys.stdin.readline().strip().split())
l = list(map(int, sys.stdin.readline().strip().split()))
l.sort()
result = list()
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    result.append(get_cnt_b(b) - get_cnt_a(a) + 1)
for i in result:
    print(i)
