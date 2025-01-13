import sys

def check(num, n):
    start = 0
    end = n-1

    while start <= end:
        mid = (start + end) // 2
        if num == nl[mid]:
            return 1
        elif num > nl[mid]:
            start = mid + 1
        elif num < nl[mid]:
            end = mid - 1
    return 0

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    nl = list(map(int, sys.stdin.readline().strip().split()))

    m = int(sys.stdin.readline().strip())
    ml = list(map(int, sys.stdin.readline().strip().split()))

    nl.sort()

    for i in ml:
        print(check(i, n))