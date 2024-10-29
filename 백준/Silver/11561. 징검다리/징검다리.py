import sys
import math

T = int(sys.stdin.readline().strip())


for _ in range(T):
    result = 0
    n = int(sys.stdin.readline().strip())

    start = 0
    end = n

    while start <= end:
        mid = (start+end) // 2
        s = mid * (mid + 1) // 2

        if s <= n:
            result = max(mid, result)
            start = mid + 1
        else:
            end = mid - 1

    print(result)