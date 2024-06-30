import sys
import heapq

n, m = map(int, sys.stdin.readline().strip().split())
l = list(map(int, sys.stdin.readline().strip().split()))
heapq.heapify(l)

for _ in range(m):
    num1 = heapq.heappop(l)
    num2 = heapq.heappop(l)

    s = num1 + num2
    heapq.heappush(l, s)
    heapq.heappush(l, s)

print(sum(l))
